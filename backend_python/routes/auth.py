from fastapi import APIRouter
from controllers.auth import login, signup

router = APIRouter()

@router.post("/login")
def create_user():
    return login()

@router.post("/signup")
def create_user():
    return signup()