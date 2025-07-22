from fastapi import APIRouter, HTTPException, Depends
from controllers import user as userController
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from config.database import get_db
from starlette import status
from utils import auth

router = APIRouter()

@router.get("/")
async def get_users(db: Session = Depends(get_db), tokenData = Depends(auth.Auth)):
    return await userController.get_all(db)

@router.get("/{id}")
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return await userController.get_by_id(id, db)

@router.put("/{id}")
async def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    return await userController.update(id, user, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db)):
    return await userController.delete(id, db)

