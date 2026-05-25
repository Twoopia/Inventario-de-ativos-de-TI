from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/", response_model=DashboardResponse, summary="Resumo geral do inventário")
def get_dashboard(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return DashboardService(db).get_summary()
