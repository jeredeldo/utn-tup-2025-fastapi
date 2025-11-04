import random
import string
from datetime import datetime, timezone, date as date_type

def generate_chasis_number() -> str:
    """Genera un número de chasis aleatorio de 17 caracteres (formato VIN)."""
    chars = string.ascii_uppercase.replace('I', '').replace('O', '').replace('Q', '') + string.digits
    return ''.join(random.choice(chars) for _ in range(17))

def is_valid_year(year: int) -> bool:
    """Valida que el año esté entre 1900 y el año actual."""
    current_year = datetime.now().year
    return 1900 <= year <= current_year

def is_valid_price(price: float) -> bool:
    """Valida que el precio sea mayor a 0."""
    return price > 0

def is_valid_future_date(date: datetime) -> bool:
    """Valida que la fecha no sea en el futuro."""
    today = datetime.now(timezone.utc).date() if date.tzinfo else datetime.now().date()
    
    if date.tzinfo:
        date_only = date.astimezone(timezone.utc).date()
    else:
        date_only = date.date()
    
    return date_only <= today

def is_valid_comprador_name(nombre: str) -> bool:
    """Valida que el nombre del comprador no esté vacío."""
    return bool(nombre and nombre.strip())
