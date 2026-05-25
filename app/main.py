import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.core.config import settings
from app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Sistema profissional de gerenciamento de ativos de TI",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    # API routes (before static files to avoid conflicts)
    app.include_router(api_router, prefix="/api/v1")

    # Static files
    app.mount("/uploads",  StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
    app.mount("/frontend", StaticFiles(directory="frontend"),           name="frontend")

    @app.get("/health", tags=["Health"])
    def health():
        return {"status": "ok"}

    # SPA catch-all — serve index.html for every non-API route
    @app.get("/{full_path:path}", include_in_schema=False)
    def spa(full_path: str):
        return FileResponse("frontend/index.html")

    return app


app = create_app()
