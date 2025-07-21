from fastapi import Request, HTTPException
import logging

# Optional: configure logging
logger = logging.getLogger("uvicorn.error")

async def handle_exception(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return server_error("An unexpected error occurred")

async def handle_http_exception(request: Request, exc: HTTPException):
    logger.warning(f"HTTP error: {exc.detail}")
    return _format_response("error", exc.detail, None, code=exc.status_code)
