from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.movement import MovementCreate, MovementResponse
from app.services.movement import MovementService

router = APIRouter(prefix="/movements", tags=["Movimentações"])


@router.post("/", response_model=MovementResponse, status_code=201, summary="Registrar movimentação")
def create_movement(
    data: MovementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return MovementService(db).create(data, created_by_id=current_user.id)


@router.get("/asset/{asset_id}", response_model=List[MovementResponse], summary="Histórico de movimentações do ativo")
def get_asset_movements(
    asset_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return MovementService(db).get_by_asset(asset_id, skip=skip, limit=limit)


@router.get("/recent", response_model=List[MovementResponse], summary="Movimentações recentes")
def get_recent_movements(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return MovementService(db).get_recent(limit=limit)


@router.get("/{movement_id}", response_model=MovementResponse, summary="Buscar movimentação por ID")
def get_movement(
    movement_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return MovementService(db).get_or_404(movement_id)
