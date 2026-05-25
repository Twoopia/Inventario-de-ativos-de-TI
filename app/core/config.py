from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Inventário de Ativos de TI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/inventario_ti"

    # Security
    SECRET_KEY: str = "change-this-to-a-very-long-random-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24h

    # File upload
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 5 * 1024 * 1024  # 5MB
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png", "gif", "webp"]

    # CORS
    CORS_ORIGINS: List[str] = ["*"]

    # First admin
    FIRST_ADMIN_EMAIL: str = "admin@empresa.com"
    FIRST_ADMIN_PASSWORD: str = "Admin@123"
    FIRST_ADMIN_NAME: str = "Administrador"

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors(cls, v):
        if isinstance(v, str):
            import json
            return json.loads(v)
        return v

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore",
    }


settings = Settings()
