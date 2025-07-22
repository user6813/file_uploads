from fastapi import FastAPI, HTTPException
from routes import router as api_router
from utils.error import handle_exception, handle_http_exception
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine, Base


# Create the FastAPI app
app = FastAPI()


# Allow CORS for all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the user router
app.include_router(api_router, prefix="/api")


# Create the database tables
Base.metadata.create_all(bind=engine)


# Dependency to get the database session
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}


# 🔧 Register global exception handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)

@app.get("/health-check")
def healthCheck():
    return { "message": "Server Running", "status": "OK" }




