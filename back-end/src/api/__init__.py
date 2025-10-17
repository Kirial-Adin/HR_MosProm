from fastapi import APIRouter

from .v1 import api_router

router = APIRouter()
router.include_router(api_router)

__all__ = ("router", )
