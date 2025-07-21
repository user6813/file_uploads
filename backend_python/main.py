from fastapi import FastAPI
from routes import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")


@app.get("/health-check")
def healthCheck():
    return { "message": "Server Running", "status": "OK" }




