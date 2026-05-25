import math
import os
from typing import Optional
from fastapi import APIRouter, Depends, File, Query, UploadFile
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin, get_current_user
from app.core.config import settings
from app.core.database import get_db
from app.models.asset import AssetStatus
from app.models.user import User
from app.schemas.asset import AssetCreate, AssetListResponse, AssetResponse, AssetUpdate, AssetFilterParams
from app.schemas.common import MessageResponse, PaginatedResponse
from app.services.asset import AssetService
from app.services.export import ExportService
from app.utils.file_upload import save_upload_file

router = APIRouter(prefix="/assets", tags=["Ativos"])


@router.post("/", response_model=AssetResponse, status_code=201, summary="Cadastrar ativo")
def create_asset(
    data: AssetCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return AssetService(db).create(data)


@router.get("/", response_model=PaginatedResponse[AssetListResponse], summary="Listar ativos")
def list_assets(
    search: Optional[str] = Query(None, description="Busca livre por tag, nome, série, marca"),
    status: Optional[AssetStatus] = Query(None),
    category_id: Optional[int] = Query(None),
    responsible_user_id: Optional[int] = Query(None),
    location: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    warranty_expired: Optional[bool] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    params = AssetFilterParams(
        search=search,
        status=status,
        category_id=category_id,
        responsible_user_id=responsible_user_id,
        location=location,
        brand=brand,
        warranty_expired=warranty_expired,
        page=page,
        page_size=page_size,
    )
    items, total = AssetService(db).list_with_filters(params)
    pages = math.ceil(total / page_size) if total > 0 else 1
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )


@router.get("/export/csv", summary="Exportar ativos em CSV")
def export_csv(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    assets = AssetService(db).get_all_for_export()
    content = ExportService().assets_to_csv(assets)
    return Response(
        content=content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=ativos_ti.csv"},
    )


@router.get("/export/excel", summary="Exportar ativos em Excel")
def export_excel(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    assets = AssetService(db).get_all_for_export()
    content = ExportService().assets_to_excel(assets)
    return Response(
        content=content,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=ativos_ti.xlsx"},
    )


@router.get("/{asset_id}", response_model=AssetResponse, summary="Buscar ativo por ID")
def get_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return AssetService(db).get_or_404(asset_id)


@router.put("/{asset_id}", response_model=AssetResponse, summary="Atualizar ativo")
def update_asset(
    asset_id: int,
    data: AssetUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return AssetService(db).update(asset_id, data)


@router.patch("/{asset_id}/status", response_model=AssetResponse, summary="Atualizar status do ativo")
def update_status(
    asset_id: int,
    status: AssetStatus,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return AssetService(db).update_status(asset_id, status)


@router.post("/{asset_id}/image", response_model=AssetResponse, summary="Upload de imagem do ativo")
async def upload_image(
    asset_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    image_path = await save_upload_file(file, subfolder="assets")
    return AssetService(db).update_image(asset_id, image_path)


@router.delete("/{asset_id}", response_model=MessageResponse, summary="Desativar ativo (soft delete)")
def delete_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    AssetService(db).delete(asset_id)
    return MessageResponse(message="Ativo desativado.")
