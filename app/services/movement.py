from typing import List, Optional
from sqlalchemy.orm import Session
from app.core.exceptions import NotFoundError
from app.models.movement import Movement
from app.repositories.movement import MovementRepository
from app.repositories.asset import AssetRepository
from app.schemas.movement import MovementCreate


class MovementService:
    def __init__(self, db: Session):
        self.repo = MovementRepository(db)
        self.asset_repo = AssetRepository(db)

    def create(self, data: MovementCreate, created_by_id: Optional[int] = None) -> Movement:
        asset = self.asset_repo.get(data.asset_id)
        if not asset:
            raise NotFoundError("Ativo")

        movement = Movement(
            asset_id=data.asset_id,
            movement_type=data.movement_type,
            from_location=data.from_location or asset.location,
            to_location=data.to_location,
            from_user_id=data.from_user_id or asset.responsible_user_id,
            to_user_id=data.to_user_id,
            notes=data.notes,
            created_by_id=created_by_id,
        )

        # Update asset state based on movement type
        from app.models.movement import MovementType
        from app.models.asset import AssetStatus

        if data.to_location:
            asset.location = data.to_location
        if data.to_user_id:
            asset.responsible_user_id = data.to_user_id

        if data.movement_type == MovementType.MAINTENANCE_IN:
            asset.status = AssetStatus.MAINTENANCE
        elif data.movement_type in (MovementType.MAINTENANCE_OUT, MovementType.RETURN):
            asset.status = AssetStatus.ACTIVE
        elif data.movement_type == MovementType.DISPOSAL:
            asset.status = AssetStatus.DISPOSED
        elif data.movement_type == MovementType.ASSIGNMENT:
            asset.status = AssetStatus.ACTIVE

        self.asset_repo.update(asset)
        return self.repo.create(movement)

    def get_by_asset(self, asset_id: int, skip: int = 0, limit: int = 50) -> List[Movement]:
        return self.repo.get_by_asset(asset_id, skip=skip, limit=limit)

    def get_recent(self, limit: int = 10) -> List[Movement]:
        return self.repo.get_recent(limit=limit)

    def get_or_404(self, movement_id: int) -> Movement:
        m = self.repo.get(movement_id)
        if not m:
            raise NotFoundError("Movimentação")
        return m
