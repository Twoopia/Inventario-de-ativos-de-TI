from fastapi import APIRouter
from app.api.v1 import auth, users, categories, assets, movements, dashboard

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(categories.router)
api_router.include_router(assets.router)
api_router.include_router(movements.router)
api_router.include_router(dashboard.router)
