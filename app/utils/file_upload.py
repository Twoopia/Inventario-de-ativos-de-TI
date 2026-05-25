import os
import uuid
from fastapi import HTTPException, UploadFile, status
from app.core.config import settings


async def save_upload_file(file: UploadFile, subfolder: str = "") -> str:
    ext = (file.filename or "").rsplit(".", 1)[-1].lower()
    if ext not in settings.ALLOWED_IMAGE_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Extensão '.{ext}' não permitida. Use: {', '.join(settings.ALLOWED_IMAGE_EXTENSIONS)}",
        )

    content = await file.read()
    if len(content) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Arquivo muito grande. Máximo: {settings.MAX_UPLOAD_SIZE // (1024*1024)}MB",
        )

    target_dir = os.path.join(settings.UPLOAD_DIR, subfolder) if subfolder else settings.UPLOAD_DIR
    os.makedirs(target_dir, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(target_dir, filename)

    with open(file_path, "wb") as f:
        f.write(content)

    relative_path = os.path.join(subfolder, filename) if subfolder else filename
    return relative_path.replace("\\", "/")


def delete_upload_file(file_path: str) -> None:
    full_path = os.path.join(settings.UPLOAD_DIR, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
