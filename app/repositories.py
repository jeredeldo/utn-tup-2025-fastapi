from typing import List, Optional, Sequence
from sqlmodel import Session, select
from sqlalchemy import func
from app.models import Auto, AutoCreate, Venta, VentaCreate


class AutoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, auto_create: AutoCreate) -> Auto:
        auto = Auto.model_validate(auto_create, from_attributes=True)
        self.session.add(auto)
        self.session.commit()
        self.session.refresh(auto)
        return auto

    def get_by_id(self, auto_id: int) -> Optional[Auto]:
        return self.session.get(Auto, auto_id)

    def get_all(self, marca: Optional[str] = None, modelo: Optional[str] = None, skip: int = 0, limit: int = 10) -> Sequence[Auto]:
        statement = select(Auto)
        if marca:
            statement = statement.where(func.lower(Auto.marca).like(f"%{marca.lower()}%"))
        if modelo:
            statement = statement.where(func.lower(Auto.modelo).like(f"%{modelo.lower()}%"))
        statement = statement.offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_by_chasis(self, numero_chasis: str) -> Optional[Auto]:
        statement = select(Auto).where(Auto.numero_chasis == numero_chasis)
        return self.session.exec(statement).first()

    def update(self, auto_id: int, auto_data: dict) -> Optional[Auto]:
        auto = self.get_by_id(auto_id)
        if not auto:
            return None
        for key, value in auto_data.items():
            setattr(auto, key, value)
        self.session.add(auto)
        self.session.commit()
        self.session.refresh(auto)
        return auto

    def delete(self, auto_id: int) -> bool:
        auto = self.get_by_id(auto_id)
        if not auto:
            return False
        self.session.delete(auto)
        self.session.commit()
        return True

    def create_multiple(self, autos: List[AutoCreate]) -> List[Auto]:
        created_autos = []
        for auto_create in autos:
            auto = self.create(auto_create)
            created_autos.append(auto)
        return created_autos

class VentaRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, venta_create: VentaCreate) -> Venta:
        venta = Venta.model_validate(venta_create, from_attributes=True)
        self.session.add(venta)
        self.session.commit()
        self.session.refresh(venta)
        return venta

    def get_by_id(self, venta_id: int) -> Optional[Venta]:
        return self.session.get(Venta, venta_id)

    def get_all(self, skip: int = 0, limit: int = 10) -> Sequence[Venta]:
        statement = select(Venta).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_by_auto_id(self, auto_id: int) -> Sequence[Venta]:
        statement = select(Venta).where(Venta.auto_id == auto_id)
        return self.session.exec(statement).all()

    def get_by_comprador(self, nombre: str) -> Sequence[Venta]:
        statement = select(Venta).where(
        func.lower(Venta.nombre_comprador).like(f"%{nombre.lower()}%")
    )
        return self.session.exec(statement).all()

    def update(self, venta_id: int, venta_data: dict) -> Optional[Venta]:
        venta = self.get_by_id(venta_id)
        if not venta:
            return None
        for key, value in venta_data.items():
            setattr(venta, key, value)
        self.session.add(venta)
        self.session.commit()
        self.session.refresh(venta)
        return venta

    def delete(self, venta_id: int) -> bool:
        venta = self.get_by_id(venta_id)
        if not venta:
            return False
        self.session.delete(venta)
        self.session.commit()
        return True

    def count_by_modelo(self, modelo: str) -> int:
        statement = select(func.count()).select_from(Venta).join(Auto).where(Auto.modelo == modelo)
        result = self.session.exec(statement).first()
        return result if result is not None else 0

    def create_multiple(self, ventas: List[VentaCreate]) -> List[Venta]:
        created_ventas = []
        for venta_create in ventas:
            venta = self.create(venta_create)
            created_ventas.append(venta)
        return created_ventas