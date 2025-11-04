from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers_autos import router as autos_router
from app.routers_ventas import router as ventas_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(autos_router)
app.include_router(ventas_router)

@app.get("/")
def read_root():
    return {"message": "API de Ventas de Autos"}