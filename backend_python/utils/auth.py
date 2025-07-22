from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils.jwt import validateToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def Auth(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    decoded_token = validateToken(token)
    return decoded_token

