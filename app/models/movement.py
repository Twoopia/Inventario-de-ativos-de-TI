import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, Enum as SAEnum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class MovementType(str, enum.Enum):
    ASSIGNMENT = "atribuicao"
    RETURN = "devolucao"
    TRANSFER = "transferencia"
    MAINTENANCE_IN = "entrada_manutencao"
    MAINTENANCE_OUT = "saida_manutencao"
    DISPOSAL = "descarte"
    ACQUISITION = "aquisicao"


class Movement(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    movement_type: Mapped[MovementType] = mapped_column(SAEnum(MovementType), index=True)
    from_location: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    to_location: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)

    # Foreign keys
    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id", ondelete="CASCADE"), index=True
    )
    from_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    to_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    created_by_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )

    # Relationships
    asset: Mapped["Asset"] = relationship("Asset", back_populates="movements")
    from_user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="movements_from", foreign_keys=[from_user_id]
    )
    to_user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="movements_to", foreign_keys=[to_user_id]
    )
    created_by: Mapped[Optional["User"]] = relationship(
        "User", back_populates="movements_created", foreign_keys=[created_by_id]
    )

    def __repr__(self) -> str:
        return f"<Movement id={self.id} asset_id={self.asset_id} type={self.movement_type}>"
