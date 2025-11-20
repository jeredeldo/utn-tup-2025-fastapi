"""FastAPI application for car sales management system.

This module sets up the main FastAPI application with database initialization,
router registration, and CORS middleware configuration.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers_autos import router as autos_router
from app.routers_ventas import router as ventas_router
from config import (
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
    DEBUG,
    CORS_ORIGINS,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events."""
    # Startup
    create_db_and_tables()
    yield
    # Shutdown


app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    lifespan=lifespan,
    debug=DEBUG,
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register application routers
app.include_router(autos_router)
app.include_router(ventas_router)


@app.get("/", tags=["health"])
def read_root():
    """Health check endpoint."""
    return {
        "status": "operational",
        "service": APP_NAME,
        "version": APP_VERSION,
    }