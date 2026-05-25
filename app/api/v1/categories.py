from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_admin, get_current_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.schemas.common import MessageResponse
from app.services.category import CategoryService

router = APIRouter(prefix="/categories", tags=["Categorias"])


@router.post("/", response_model=CategoryResponse, status_code=201, summary="Criar categoria")
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    return CategoryService(db).create(data)


@router.get("/", response_model=List[CategoryResponse], summary="Listar categorias")
def list_categories(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    rows = CategoryService(db).get_all_with_count()
    return [CategoryResponse(**r) for r in rows]


@router.get("/{category_id}", response_model=CategoryResponse, summary="Buscar categoria")
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    cat = CategoryService(db).get_or_404(category_id)
    return CategoryResponse(
        id=cat.id,
        name=cat.name,
        description=cat.description,
        created_at=cat.created_at,
        asset_count=len(cat.assets),
    )


@router.put("/{category_id}", response_model=CategoryResponse, summary="Atualizar categoria")
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    cat = CategoryService(db).update(category_id, data)
    return CategoryResponse(
        id=cat.id,
        name=cat.name,
        description=cat.description,
        created_at=cat.created_at,
        asset_count=len(cat.assets),
    )


@router.delete("/{category_id}", response_model=MessageResponse, summary="Remover categoria")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    CategoryService(db).delete(category_id)
    return MessageResponse(message="Categoria removida.")
