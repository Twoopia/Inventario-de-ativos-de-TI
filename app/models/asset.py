import enum
from datetime import date, datetime
from typing import List, Optional
from sqlalchemy import (
    Boolean, Date, DateTime, Enum as SAEnum,
    Float, ForeignKey, Integer, String, Text, func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class AssetStatus(str, enum.Enum):
    ACTIVE = "ativo"
    INACTIVE = "inativo"
    MAINTENANCE = "manutencao"
    DISPOSED = "descartado"
    LOST = "perdido"
    RESERVED = "reservado"


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tag: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    serial_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True)
    brand: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    model: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    status: Mapped[AssetStatus] = mapped_column(
        SAEnum(AssetStatus), default=AssetStatus.ACTIVE, index=True
    )
    location: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    purchase_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    purchase_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    warranty_expires: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    image_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    # Foreign keys
    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True
    )
    responsible_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )

    # Relationships
    category: Mapped[Optional["Category"]] = relationship("Category", back_populates="assets")
    responsible_user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="assets", foreign_keys=[responsible_user_id]
    )
    movements: Mapped[List["Movement"]] = relationship(
        "Movement", back_populates="asset", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Asset id={self.id} tag={self.tag} name={self.name}>"
