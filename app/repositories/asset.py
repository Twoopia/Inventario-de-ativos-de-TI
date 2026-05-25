from datetime import date
from typing import List, Optional, Tuple
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import Session, joinedload
from app.models.asset import Asset, AssetStatus
from app.repositories.base import BaseRepository


class AssetRepository(BaseRepository[Asset]):
    def __init__(self, db: Session):
        super().__init__(Asset, db)

    def get_with_relations(self, asset_id: int) -> Optional[Asset]:
        return (
            self.db.query(Asset)
            .options(
                joinedload(Asset.category),
                joinedload(Asset.responsible_user),
            )
            .filter(Asset.id == asset_id)
            .first()
        )

    def get_by_tag(self, tag: str) -> Optional[Asset]:
        return self.db.query(Asset).filter(Asset.tag == tag).first()

    def get_by_serial(self, serial_number: str) -> Optional[Asset]:
        return (
            self.db.query(Asset)
            .filter(Asset.serial_number == serial_number)
            .first()
        )

    def search_and_filter(
        self,
        search: Optional[str] = None,
        status: Optional[AssetStatus] = None,
        category_id: Optional[int] = None,
        responsible_user_id: Optional[int] = None,
        location: Optional[str] = None,
        brand: Optional[str] = None,
        warranty_expired: Optional[bool] = None,
        only_active: bool = True,
        skip: int = 0,
        limit: int = 20,
    ) -> Tuple[List[Asset], int]:
        query = self.db.query(Asset).options(
            joinedload(Asset.category),
            joinedload(Asset.responsible_user),
        )

        if only_active:
            query = query.filter(Asset.is_active == True)
        if search:
            term = f"%{search}%"
            query = query.filter(
                or_(
                    Asset.tag.ilike(term),
                    Asset.name.ilike(term),
                    Asset.serial_number.ilike(term),
                    Asset.brand.ilike(term),
                    Asset.model.ilike(term),
                    Asset.location.ilike(term),
                )
            )
        if status:
            query = query.filter(Asset.status == status)
        if category_id:
            query = query.filter(Asset.category_id == category_id)
        if responsible_user_id:
            query = query.filter(Asset.responsible_user_id == responsible_user_id)
        if location:
            query = query.filter(Asset.location.ilike(f"%{location}%"))
        if brand:
            query = query.filter(Asset.brand.ilike(f"%{brand}%"))
        if warranty_expired is True:
            query = query.filter(
                and_(Asset.warranty_expires != None, Asset.warranty_expires < date.today())
            )
        elif warranty_expired is False:
            query = query.filter(
                or_(
                    Asset.warranty_expires == None,
                    Asset.warranty_expires >= date.today(),
                )
            )

        total = query.count()
        items = query.order_by(Asset.updated_at.desc()).offset(skip).limit(limit).all()
        return items, total

    def get_stats_by_status(self) -> List[dict]:
        rows = (
            self.db.query(Asset.status, func.count(Asset.id).label("count"))
            .filter(Asset.is_active == True)
            .group_by(Asset.status)
            .all()
        )
        return [{"status": r.status, "count": r.count} for r in rows]

    def count_without_responsible(self) -> int:
        return (
            self.db.query(Asset)
            .filter(Asset.responsible_user_id == None, Asset.is_active == True)
            .count()
        )

    def count_warranty_expiring(self, days: int = 30) -> int:
        from datetime import timedelta
        future = date.today() + timedelta(days=days)
        return (
            self.db.query(Asset)
            .filter(
                Asset.warranty_expires != None,
                Asset.warranty_expires <= future,
                Asset.warranty_expires >= date.today(),
                Asset.is_active == True,
            )
            .count()
        )

    def sum_total_value(self) -> float:
        result = (
            self.db.query(func.sum(Asset.purchase_value))
            .filter(Asset.is_active == True)
            .scalar()
        )
        return float(result or 0)
