from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_current_admin, get_current_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.common import MessageResponse
from app.schemas.user import UserCreate, UserPasswordUpdate, UserResponse, UserUpdate
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Usuários"])


@router.post("/", response_model=UserResponse, status_code=201, summary="Criar usuário")
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    return UserService(db).create(data)


@router.get("/", response_model=List[UserResponse], summary="Listar usuários")
def list_users(
    search: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    svc = UserService(db)
    if search:
        return svc.search(search, skip=skip, limit=limit)
    return svc.get_all(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse, summary="Buscar usuário por ID")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return UserService(db).get_or_404(user_id)


@router.put("/{user_id}", response_model=UserResponse, summary="Atualizar usuário")
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    return UserService(db).update(user_id, data)


@router.patch("/{user_id}/password", response_model=MessageResponse, summary="Alterar senha")
def change_password(
    user_id: int,
    data: UserPasswordUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id and not current_user.is_admin:
        from app.core.exceptions import ForbiddenError
        raise ForbiddenError("Você não pode alterar a senha de outro usuário.")
    UserService(db).update_password(user_id, data)
    return MessageResponse(message="Senha alterada com sucesso.")


@router.delete("/{user_id}", response_model=MessageResponse, summary="Desativar usuário")
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    UserService(db).deactivate(user_id)
    return MessageResponse(message="Usuário desativado.")
