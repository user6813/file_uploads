from fastapi.responses import JSONResponse
from fastapi import status
from typing import Any, Optional


def _format_response(status_bool: bool, message: str, data: Optional[Any] = None, code: int = 200):
    return JSONResponse(
        status_code=code,
        content={
            "success": status_bool,
            "message": message,
            "data": data
        }
    )

# ✅ Success responses
def ok(data: Any = None, message: str = "Success"):
    return _format_response(True, message, data, code=status.HTTP_200_OK)

def created(data: Any = None, message: str = "Resource created"):
    return _format_response(True, message, data, code=status.HTTP_201_CREATED)

# ❌ Error responses
def bad_request(message: str = "Bad request"):
    return _format_response(False, message, None, code=status.HTTP_400_BAD_REQUEST)

def unauthorized(message: str = "Unauthorized"):
    return _format_response(False, message, None, code=status.HTTP_401_UNAUTHORIZED)

def forbidden(message: str = "Forbidden"):
    return _format_response(False, message, None, code=status.HTTP_403_FORBIDDEN)

def not_found(message: str = "Not found"):
    return _format_response(False, message, None, code=status.HTTP_404_NOT_FOUND)

def server_error(message: str = "Internal server error"):
    return _format_response(False, message, None, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
