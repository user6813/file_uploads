from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserBase(UserLogin):
    name: str
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int



    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    token_type: str