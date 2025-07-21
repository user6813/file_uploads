from fastapi import FastAPI
from routes import router as api_router
from utils.error import handle_exception, handle_http_exception

app = FastAPI()
app.include_router(api_router, prefix="/api")


# 🔧 Register global exception handlers
app.add_exception_handler(Exception, handle_exception)
# app.add_exception_handler(HTTPException, handle_http_exception)

@app.get("/health-check")
def healthCheck():
    return { "message": "Server Running", "status": "OK" }




