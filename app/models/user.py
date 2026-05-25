from datetime import datetime
from typing import List, Optional
from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    department: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    assets: Mapped[List["Asset"]] = relationship(
        "Asset", back_populates="responsible_user", foreign_keys="Asset.responsible_user_id"
    )
    movements_from: Mapped[List["Movement"]] = relationship(
        "Movement", back_populates="from_user", foreign_keys="Movement.from_user_id"
    )
    movements_to: Mapped[List["Movement"]] = relationship(
        "Movement", back_populates="to_user", foreign_keys="Movement.to_user_id"
    )
    movements_created: Mapped[List["Movement"]] = relationship(
        "Movement", back_populates="created_by", foreign_keys="Movement.created_by_id"
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"
