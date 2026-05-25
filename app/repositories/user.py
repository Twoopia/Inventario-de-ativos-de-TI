from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_active_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return (
            self.db.query(User)
            .filter(User.is_active == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search(self, query: str, skip: int = 0, limit: int = 100) -> List[User]:
        term = f"%{query}%"
        return (
            self.db.query(User)
            .filter(
                (User.name.ilike(term))
                | (User.email.ilike(term))
                | (User.department.ilike(term))
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    def count_active(self) -> int:
        return self.db.query(User).filter(User.is_active == True).count()
