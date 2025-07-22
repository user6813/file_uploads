from fastapi import APIRouter, HTTPException, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.user import UserLogin
from controllers import user as userController
from schemas.user import UserCreate
from starlette import status

router = APIRouter()

@router.post("/login")
async def login(user: UserLogin,db: Session = Depends(get_db)):
    return await userController.userLogin(user ,db)

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    return await userController.add(user, db)
