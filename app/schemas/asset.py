from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from app.models.asset import AssetStatus
from app.schemas.category import CategoryResponse
from app.schemas.user import UserResponse


class AssetBase(BaseModel):
    tag: str
    name: str
    description: Optional[str] = None
    serial_number: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    status: AssetStatus = AssetStatus.ACTIVE
    location: Optional[str] = None
    purchase_date: Optional[date] = None
    purchase_value: Optional[float] = None
    warranty_expires: Optional[date] = None
    notes: Optional[str] = None
    category_id: Optional[int] = None
    responsible_user_id: Optional[int] = None


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    serial_number: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    status: Optional[AssetStatus] = None
    location: Optional[str] = None
    purchase_date: Optional[date] = None
    purchase_value: Optional[float] = None
    warranty_expires: Optional[date] = None
    notes: Optional[str] = None
    category_id: Optional[int] = None
    responsible_user_id: Optional[int] = None
    is_active: Optional[bool] = None


class AssetResponse(AssetBase):
    id: int
    image_path: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    category: Optional[CategoryResponse] = None
    responsible_user: Optional[UserResponse] = None

    model_config = {"from_attributes": True}


class AssetListResponse(BaseModel):
    id: int
    tag: str
    name: str
    status: AssetStatus
    brand: Optional[str] = None
    model: Optional[str] = None
    location: Optional[str] = None
    image_path: Optional[str] = None
    category: Optional[CategoryResponse] = None
    responsible_user: Optional[UserResponse] = None
    updated_at: datetime

    model_config = {"from_attributes": True}


class AssetFilterParams(BaseModel):
    search: Optional[str] = None
    status: Optional[AssetStatus] = None
    category_id: Optional[int] = None
    responsible_user_id: Optional[int] = None
    location: Optional[str] = None
    brand: Optional[str] = None
    warranty_expired: Optional[bool] = None
    page: int = 1
    page_size: int = 20
