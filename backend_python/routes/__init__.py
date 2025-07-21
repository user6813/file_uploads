from fastapi import APIRouter
from .user import router as user_router
from .files import router as file_router

router = APIRouter()
router.include_router(user_router, prefix="/user")
router.include_router(file_router, prefix="/file")
