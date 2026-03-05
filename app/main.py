from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import employees, attendance

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(employees.router)
app.include_router(attendance.router)

# Health check
@app.get("/")
def health():
    return {"status": "HRMS API Running"}