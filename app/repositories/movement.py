from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.movement import Movement, MovementType
from app.repositories.base import BaseRepository


class MovementRepository(BaseRepository[Movement]):
    def __init__(self, db: Session):
        super().__init__(Movement, db)

    def get_by_asset(
        self, asset_id: int, skip: int = 0, limit: int = 50
    ) -> List[Movement]:
        return (
            self.db.query(Movement)
            .options(
                joinedload(Movement.from_user),
                joinedload(Movement.to_user),
                joinedload(Movement.created_by),
            )
            .filter(Movement.asset_id == asset_id)
            .order_by(Movement.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_recent(self, limit: int = 10) -> List[Movement]:
        return (
            self.db.query(Movement)
            .options(
                joinedload(Movement.asset),
                joinedload(Movement.created_by),
            )
            .order_by(Movement.created_at.desc())
            .limit(limit)
            .all()
        )

    def count_by_asset(self, asset_id: int) -> int:
        return (
            self.db.query(Movement)
            .filter(Movement.asset_id == asset_id)
            .count()
        )
