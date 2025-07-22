from fastapi import HTTPException
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenSchema
from sqlalchemy.orm import Session
from utils.bcrypt import createHash, compareHash
from utils.jwt import createAccessToken
from starlette import status
from utils.errorWrapper import error_wrapper
from utils import response

@error_wrapper
async def get_all(db: Session):
    db_user = db.query(User).all()
    return db_user


@error_wrapper
async def get_by_id(id: int, db: Session):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user is None:
        return response.not_found("User Not found")
    return response.ok(db_user)


@error_wrapper
async def add(user: UserCreate, db: Session):
    db_user = User(name=user.name, email=user.email, password=createHash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return response.created(db_user)


@error_wrapper
async def update(id: int, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == id).first()
    db_user.name = user.name
    db.commit()
    db.refresh(db_user)
    return response.ok(db_user)


@error_wrapper
async def delete(id: int, db: Session):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(db_user)
    db.commit()
    return response.ok(db_user)

@error_wrapper
async def userLogin(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user and compareHash(user.password, db_user.password):
        token = createAccessToken({ "userId": db_user.id })
        return TokenSchema(access_token=token, token_type="bearer")
    else:
        return response.unauthorized("Invalid credentials")
