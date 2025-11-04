from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from pydantic import field_validator
from app.utils import is_valid_year, is_valid_price, is_valid_future_date, is_valid_comprador_name


class AutoBase(SQLModel):
    marca: str
    modelo: str
    año: int
    numero_chasis: str

class Auto(AutoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ventas: List["Venta"] = Relationship(back_populates="auto")

class AutoCreate(SQLModel):
    marca: str
    modelo: str
    año: int

    @field_validator("año")
    @classmethod
    def validate_year(cls, v):
        if not is_valid_year(v):
            raise ValueError("El año debe estar entre 1900 y el año actual.")
        return v

class AutoRead(AutoBase):
    id: int

class AutoUpdate(SQLModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    año: Optional[int] = None

    @field_validator("año")
    @classmethod
    def validate_year(cls, v):
        if v is not None and not is_valid_year(v):
            raise ValueError("El año debe estar entre 1900 y el año actual.")
        return v

class AutoReadWithVentas(AutoRead):
    ventas: List["VentaRead"] = []


class VentaBase(SQLModel):
    nombre_comprador: str
    precio: float
    fecha_venta: datetime

class Venta(VentaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    auto_id: int = Field(foreign_key="auto.id")
    auto: Optional[Auto] = Relationship(back_populates="ventas")

class VentaCreate(VentaBase):
    auto_id: int

    @field_validator("nombre_comprador")
    @classmethod
    def validate_comprador_name(cls, v):
        if not is_valid_comprador_name(v):
            raise ValueError("El nombre del comprador no puede estar vacío.")
        return v

    @field_validator("precio")
    @classmethod
    def validate_price(cls, v):
        if not is_valid_price(v):
            raise ValueError("El precio debe ser mayor a 0.")
        return v

    @field_validator("fecha_venta")
    @classmethod
    def validate_fecha_venta(cls, v):
        if not is_valid_future_date(v):
            raise ValueError("La fecha de venta no puede ser en el futuro.")
        return v

class VentaRead(VentaBase):
    id: int
    auto_id: int

class VentaUpdate(SQLModel):
    nombre_comprador: Optional[str] = None
    precio: Optional[float] = None
    fecha_venta: Optional[datetime] = None

    @field_validator("nombre_comprador")
    @classmethod
    def validate_comprador_name(cls, v):
        if v is not None and not is_valid_comprador_name(v):
            raise ValueError("El nombre del comprador no puede estar vacío.")
        return v

    @field_validator("precio")
    @classmethod
    def validate_price(cls, v):
        if v is not None and not is_valid_price(v):
            raise ValueError("El precio debe ser mayor a 0.")
        return v

    @field_validator("fecha_venta")
    @classmethod
    def validate_fecha_venta(cls, v):
        if v is not None and not is_valid_future_date(v):
            raise ValueError("La fecha de venta no puede ser en el futuro.")
        return v

class VentaReadWithAuto(VentaRead):
    auto: Optional[AutoRead] = None