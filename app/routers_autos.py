from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Sequence, Optional
from app.database import get_session
from app.models import Auto, AutoCreate, AutoRead, AutoReadWithVentas, AutoUpdate
from app.repositories import AutoRepository
from app.utils import generate_chasis_number

router = APIRouter(prefix="/autos", tags=["autos"])

def get_auto_repo(session: Session = Depends(get_session)):
    return AutoRepository(session)

@router.post("/", response_model=AutoRead, status_code=status.HTTP_201_CREATED)
def create_auto(auto: AutoCreate, repo: AutoRepository = Depends(get_auto_repo)):
    while True:
        numero_chasis = generate_chasis_number()
        if not repo.get_by_chasis(numero_chasis):
            break
    
    auto_dict = auto.model_dump()
    auto_dict["numero_chasis"] = numero_chasis
    auto_completo = Auto(**auto_dict)
    
    repo.session.add(auto_completo)
    repo.session.commit()
    repo.session.refresh(auto_completo)
    
    return auto_completo

@router.post("/batch/", response_model=Sequence[AutoRead], status_code=status.HTTP_201_CREATED)
def create_multiple_autos(autos: list[AutoCreate], repo: AutoRepository = Depends(get_auto_repo)):
    created_autos = []
    for auto in autos:
        while True:
            numero_chasis = generate_chasis_number()
            if not repo.get_by_chasis(numero_chasis):
                break
        
        auto_dict = auto.model_dump()
        auto_dict["numero_chasis"] = numero_chasis
        auto_completo = Auto(**auto_dict)
        
        repo.session.add(auto_completo)
        repo.session.flush()
        created_autos.append(auto_completo)
    
    repo.session.commit()
    for auto_obj in created_autos:
        repo.session.refresh(auto_obj)
    
    return created_autos

@router.get("/", response_model=Sequence[AutoRead])
def list_autos(
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    skip: int = 0, 
    limit: int = 10, 
    repo: AutoRepository = Depends(get_auto_repo)
):
    return repo.get_all(marca=marca, modelo=modelo, skip=skip, limit=limit)

@router.get("/chasis/{numero_chasis}", response_model=AutoRead)
def get_auto_by_chasis(numero_chasis: str, repo: AutoRepository = Depends(get_auto_repo)):
    auto = repo.get_by_chasis(numero_chasis)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado con ese número de chasis.")
    return auto

@router.get("/{auto_id}", response_model=AutoRead)
def get_auto(auto_id: int, repo: AutoRepository = Depends(get_auto_repo)):
    auto = repo.get_by_id(auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    return auto

@router.get("/{auto_id}/with-ventas", response_model=AutoReadWithVentas)
def get_auto_with_ventas(auto_id: int, repo: AutoRepository = Depends(get_auto_repo)):
    auto = repo.get_by_id(auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    return auto

@router.put("/{auto_id}", response_model=AutoRead)
def update_auto(auto_id: int, auto_update: AutoUpdate, repo: AutoRepository = Depends(get_auto_repo)):
    auto = repo.get_by_id(auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    
    update_data = auto_update.model_dump(exclude_unset=True)
    return repo.update(auto_id, update_data)

@router.delete("/{auto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auto(auto_id: int, repo: AutoRepository = Depends(get_auto_repo)):
    if not repo.delete(auto_id):
        raise HTTPException(status_code=404, detail="Auto no encontrado.")
    return None