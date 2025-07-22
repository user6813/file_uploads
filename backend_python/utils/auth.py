from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils.jwt import validateToken
from utils import response

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def Auth():
    return True
    print("TOKEN",token)
    if not token:
        return response.unauthorized("Not authenticated")
    decoded_token = validateToken(token)
    return decoded_token

