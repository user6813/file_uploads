from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
import jwt
from starlette import status

SECRET_KEY = "qwertyuiopasdfghjklzxcvbnm"

ALGORITHM = "HS256"

def createAccessToken(data: dict, expires_delta:timedelta = timedelta(minutes=15)):
    payload = { "data": data }
    expires = datetime.now(timezone.utc) + expires_delta
    payload.update({ 'exp': expires })
    token = jwt.encode(
        algorithm=ALGORITHM,
        key=SECRET_KEY,
        payload=payload
    )
    return token

def validateToken(token):
    try:
        payload = jwt.decode(
            token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        # Optional: check if token is expired manually
        if payload.get("exp") and payload["exp"] < datetime.now(timezone.utc).timestamp():
            return None
        return payload["data"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.PyJWKError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")