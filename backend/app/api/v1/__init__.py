from fastapi import APIRouter

from .auth import router as auth_router
from .reports import router as report_router
from .evidence import router as evidence_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(report_router)
api_router.include_router(evidence_router)