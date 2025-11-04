from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Sequence, Optional

from app.database import get_session
from app.models import Venta, VentaCreate, VentaRead, VentaReadWithAuto, VentaUpdate
from app.repositories import VentaRepository, AutoRepository

router = APIRouter(prefix="/ventas", tags=["ventas"])

def get_venta_repo(session: Session = Depends(get_session)):
    return VentaRepository(session)

def get_auto_repo(session: Session = Depends(get_session)):
    return AutoRepository(session)

@router.post("/", response_model=VentaReadWithAuto, status_code=status.HTTP_201_CREATED)
def create_venta(venta: VentaCreate, 
                 repo: VentaRepository = Depends(get_venta_repo),
                 auto_repo: AutoRepository = Depends(get_auto_repo)):
    if not auto_repo.get_by_id(venta.auto_id):
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    return repo.create(venta)

@router.post("/batch/", response_model=Sequence[VentaReadWithAuto], status_code=status.HTTP_201_CREATED)
def create_multiple_ventas(ventas: list[VentaCreate], 
                          repo: VentaRepository = Depends(get_venta_repo),
                          auto_repo: AutoRepository = Depends(get_auto_repo)):
    for venta in ventas:
        if not auto_repo.get_by_id(venta.auto_id):
            raise HTTPException(status_code=404, detail=f"Auto con ID {venta.auto_id} no encontrado.")
    return repo.create_multiple(ventas)

@router.get("/", response_model=Sequence[VentaReadWithAuto])
def list_ventas(skip: int = 0, limit: int = 10, repo: VentaRepository = Depends(get_venta_repo)):
    return repo.get_all(skip=skip, limit=limit)

@router.get("/auto/{auto_id}", response_model=Sequence[VentaReadWithAuto])
def get_ventas_by_auto(auto_id: int, repo: VentaRepository = Depends(get_venta_repo), auto_repo: AutoRepository = Depends(get_auto_repo)):
    if not auto_repo.get_by_id(auto_id):
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    return repo.get_by_auto_id(auto_id)

@router.get("/comprador/{nombre}", response_model=Sequence[VentaReadWithAuto])
def get_ventas_by_comprador(nombre: str, repo: VentaRepository = Depends(get_venta_repo)):
    return repo.get_by_comprador(nombre)

@router.get("/{venta_id}", response_model=VentaReadWithAuto)
def get_venta(venta_id: int, repo: VentaRepository = Depends(get_venta_repo)):
    venta = repo.get_by_id(venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada.")
    return venta

@router.put("/{venta_id}", response_model=VentaRead)
def update_venta(venta_id: int, venta_update: VentaUpdate, repo: VentaRepository = Depends(get_venta_repo)):
    venta = repo.get_by_id(venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada.")
    
    update_data = venta_update.model_dump(exclude_unset=True)
    return repo.update(venta_id, update_data)

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venta(venta_id: int, repo: VentaRepository = Depends(get_venta_repo)):
    if not repo.delete(venta_id):
        raise HTTPException(status_code=404, detail="Venta no encontrada.")
    return None