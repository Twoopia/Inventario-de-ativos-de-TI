from typing import List, Optional
from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError, UnauthorizedError
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserPasswordUpdate


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create(self, data: UserCreate) -> User:
        if self.repo.get_by_email(data.email):
            raise ConflictError(f"E-mail '{data.email}' já cadastrado.")
        user = User(
            name=data.name,
            email=data.email,
            hashed_password=get_password_hash(data.password),
            department=data.department,
            phone=data.phone,
            is_admin=data.is_admin,
        )
        return self.repo.create(user)

    def get_or_404(self, user_id: int) -> User:
        user = self.repo.get(user_id)
        if not user:
            raise NotFoundError("Usuário")
        return user

    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.repo.get_all(skip=skip, limit=limit)

    def search(self, query: str, skip: int = 0, limit: int = 50) -> List[User]:
        return self.repo.search(query, skip=skip, limit=limit)

    def update(self, user_id: int, data: UserUpdate) -> User:
        user = self.get_or_404(user_id)
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(user, field, value)
        return self.repo.update(user)

    def update_password(self, user_id: int, data: UserPasswordUpdate) -> User:
        user = self.get_or_404(user_id)
        if not verify_password(data.current_password, user.hashed_password):
            raise UnauthorizedError("Senha atual incorreta.")
        user.hashed_password = get_password_hash(data.new_password)
        return self.repo.update(user)

    def deactivate(self, user_id: int) -> User:
        user = self.get_or_404(user_id)
        user.is_active = False
        return self.repo.update(user)

    def authenticate(self, email: str, password: str) -> Optional[User]:
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        if not user.is_active:
            return None
        return user

    def create_first_admin(self, email: str, password: str, name: str) -> Optional[User]:
        if self.repo.get_by_email(email):
            return None
        user = User(
            name=name,
            email=email,
            hashed_password=get_password_hash(password),
            is_admin=True,
            is_active=True,
        )
        return self.repo.create(user)
