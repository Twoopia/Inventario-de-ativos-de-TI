from typing import Dict, List
from pydantic import BaseModel


class StatusCount(BaseModel):
    status: str
    count: int


class CategoryCount(BaseModel):
    category: str
    count: int


class RecentMovement(BaseModel):
    id: int
    asset_tag: str
    asset_name: str
    movement_type: str
    created_at: str
    created_by: str


class DashboardResponse(BaseModel):
    total_assets: int
    active_assets: int
    inactive_assets: int
    maintenance_assets: int
    disposed_assets: int
    lost_assets: int
    reserved_assets: int
    total_value: float
    assets_by_status: List[StatusCount]
    assets_by_category: List[CategoryCount]
    recent_movements: List[RecentMovement]
    warranty_expiring_soon: int
    assets_without_responsible: int
