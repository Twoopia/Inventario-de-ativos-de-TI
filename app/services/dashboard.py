from sqlalchemy.orm import Session
from app.models.asset import AssetStatus
from app.repositories.asset import AssetRepository
from app.repositories.category import CategoryRepository
from app.repositories.movement import MovementRepository
from app.schemas.dashboard import (
    CategoryCount,
    DashboardResponse,
    RecentMovement,
    StatusCount,
)


class DashboardService:
    def __init__(self, db: Session):
        self.asset_repo = AssetRepository(db)
        self.category_repo = CategoryRepository(db)
        self.movement_repo = MovementRepository(db)

    def get_summary(self) -> DashboardResponse:
        status_counts = {r["status"]: r["count"] for r in self.asset_repo.get_stats_by_status()}

        assets_by_status = [
            StatusCount(status=s.value, count=status_counts.get(s, 0))
            for s in AssetStatus
        ]

        cats_with_count = self.category_repo.get_all_with_count()
        assets_by_category = [
            CategoryCount(category=c["name"], count=c["asset_count"])
            for c in cats_with_count
            if c["asset_count"] > 0
        ]

        recent_raw = self.movement_repo.get_recent(limit=10)
        recent_movements = []
        for m in recent_raw:
            recent_movements.append(
                RecentMovement(
                    id=m.id,
                    asset_tag=m.asset.tag if m.asset else "—",
                    asset_name=m.asset.name if m.asset else "—",
                    movement_type=m.movement_type.value,
                    created_at=m.created_at.strftime("%d/%m/%Y %H:%M"),
                    created_by=m.created_by.name if m.created_by else "Sistema",
                )
            )

        total = sum(r["count"] for r in self.asset_repo.get_stats_by_status())

        return DashboardResponse(
            total_assets=total,
            active_assets=status_counts.get(AssetStatus.ACTIVE, 0),
            inactive_assets=status_counts.get(AssetStatus.INACTIVE, 0),
            maintenance_assets=status_counts.get(AssetStatus.MAINTENANCE, 0),
            disposed_assets=status_counts.get(AssetStatus.DISPOSED, 0),
            lost_assets=status_counts.get(AssetStatus.LOST, 0),
            reserved_assets=status_counts.get(AssetStatus.RESERVED, 0),
            total_value=self.asset_repo.sum_total_value(),
            assets_by_status=assets_by_status,
            assets_by_category=assets_by_category,
            recent_movements=recent_movements,
            warranty_expiring_soon=self.asset_repo.count_warranty_expiring(30),
            assets_without_responsible=self.asset_repo.count_without_responsible(),
        )
