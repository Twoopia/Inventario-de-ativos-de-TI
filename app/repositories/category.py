from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db: Session):
        super().__init__(Category, db)

    def get_by_name(self, name: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.name == name).first()

    def get_all_with_count(self) -> List[dict]:
        rows = (
            self.db.query(Category, func.count(Asset.id).label("asset_count"))
            .outerjoin(Asset, Asset.category_id == Category.id)
            .group_by(Category.id)
            .order_by(Category.name)
            .all()
        )
        result = []
        for cat, count in rows:
            data = {
                "id": cat.id,
                "name": cat.name,
                "description": cat.description,
                "created_at": cat.created_at,
                "asset_count": count,
            }
            result.append(data)
        return result
