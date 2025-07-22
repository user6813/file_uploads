from functools import wraps
from fastapi import HTTPException, status
import logging
from utils import response

def error_wrapper(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as http_exc:
            # Re-raise FastAPI exceptions
            raise http_exc
        except Exception as e:
            logging.exception("Unexpected error occurred")
            return response.server_error(f"Something went wrong. Please try again later.\n {e}",error=e)
    return wrapper
