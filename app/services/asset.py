from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.asset import Asset, AssetStatus
from app.repositories.asset import AssetRepository
from app.schemas.asset import AssetCreate, AssetFilterParams, AssetUpdate


class AssetService:
    def __init__(self, db: Session):
        self.repo = AssetRepository(db)

    def create(self, data: AssetCreate) -> Asset:
        if self.repo.get_by_tag(data.tag):
            raise ConflictError(f"Tag '{data.tag}' já cadastrada.")
        if data.serial_number and self.repo.get_by_serial(data.serial_number):
            raise ConflictError(f"Número de série '{data.serial_number}' já cadastrado.")
        asset = Asset(**data.model_dump())
        return self.repo.create(asset)

    def get_or_404(self, asset_id: int) -> Asset:
        asset = self.repo.get_with_relations(asset_id)
        if not asset:
            raise NotFoundError("Ativo")
        return asset

    def list_with_filters(
        self, params: AssetFilterParams
    ) -> Tuple[List[Asset], int]:
        skip = (params.page - 1) * params.page_size
        return self.repo.search_and_filter(
            search=params.search,
            status=params.status,
            category_id=params.category_id,
            responsible_user_id=params.responsible_user_id,
            location=params.location,
            brand=params.brand,
            warranty_expired=params.warranty_expired,
            skip=skip,
            limit=params.page_size,
        )

    def update(self, asset_id: int, data: AssetUpdate) -> Asset:
        asset = self.get_or_404(asset_id)
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(asset, field, value)
        return self.repo.update(asset)

    def update_status(self, asset_id: int, status: AssetStatus) -> Asset:
        asset = self.get_or_404(asset_id)
        asset.status = status
        return self.repo.update(asset)

    def update_image(self, asset_id: int, image_path: str) -> Asset:
        asset = self.get_or_404(asset_id)
        asset.image_path = image_path
        return self.repo.update(asset)

    def delete(self, asset_id: int) -> None:
        asset = self.get_or_404(asset_id)
        asset.is_active = False
        self.repo.update(asset)

    def get_all_for_export(self) -> List[Asset]:
        items, _ = self.repo.search_and_filter(limit=99999, skip=0)
        return items
