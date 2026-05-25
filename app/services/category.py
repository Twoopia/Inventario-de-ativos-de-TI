from typing import List
from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.category import Category
from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, db: Session):
        self.repo = CategoryRepository(db)

    def create(self, data: CategoryCreate) -> Category:
        if self.repo.get_by_name(data.name):
            raise ConflictError(f"Categoria '{data.name}' já existe.")
        category = Category(name=data.name, description=data.description)
        return self.repo.create(category)

    def get_or_404(self, category_id: int) -> Category:
        cat = self.repo.get(category_id)
        if not cat:
            raise NotFoundError("Categoria")
        return cat

    def get_all_with_count(self) -> List[dict]:
        return self.repo.get_all_with_count()

    def update(self, category_id: int, data: CategoryUpdate) -> Category:
        cat = self.get_or_404(category_id)
        if data.name and data.name != cat.name:
            if self.repo.get_by_name(data.name):
                raise ConflictError(f"Categoria '{data.name}' já existe.")
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(cat, field, value)
        return self.repo.update(cat)

    def delete(self, category_id: int) -> None:
        cat = self.get_or_404(category_id)
        self.repo.delete(cat)
