from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.models.movement import MovementType
from app.schemas.user import UserResponse


class MovementBase(BaseModel):
    movement_type: MovementType
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    notes: Optional[str] = None
    from_user_id: Optional[int] = None
    to_user_id: Optional[int] = None


class MovementCreate(MovementBase):
    asset_id: int


class MovementResponse(MovementBase):
    id: int
    asset_id: int
    created_at: datetime
    created_by_id: Optional[int] = None
    from_user: Optional[UserResponse] = None
    to_user: Optional[UserResponse] = None
    created_by: Optional[UserResponse] = None

    model_config = {"from_attributes": True}
