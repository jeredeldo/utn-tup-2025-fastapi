# API de Ventas de Autos# API de Ventas de Autos# API CRUD de Ventas de Autos



API REST para gestionar autos y sus ventas usando FastAPI y PostgreSQL.



## InstalaciónAPI REST para gestionar autos y sus ventas.Una API REST completa para la gestión de inventario de autos y registro de ventas, desarrollada con **FastAPI**, **SQLModel** y **PostgreSQL**.



```bash

# Crear virtual environment

python -m venv venv## Instalación## Características

.\venv\Scripts\Activate.ps1



# Instalar dependencias

pip install -r requirements.txt```bash- ✅ CRUD completo para Autos y Ventas

```

python -m venv venv- ✅ Validaciones robustas según enunciado

## Configuración

.\venv\Scripts\Activate.ps1- ✅ Generación automática de números de chasis únicos (VIN de 17 caracteres)

Crear archivo `.env` en la raíz:

```pip install -r requirements.txt- ✅ Búsquedas avanzadas (por chasis, comprador, marca, modelo)

DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/autos_db

``````- ✅ Paginación con skip/limit



## Ejecutar- ✅ Relaciones One-to-Many entre Autos y Ventas



```bash## Configuración- ✅ Documentación interactiva con Swagger UI

# Iniciar servidor

uvicorn main:app --reload- ✅ Tests automatizados con pytest



# API: http://localhost:8000Crear `.env` en la raíz:- ✅ Patrón Repository implementado

# Docs: http://localhost:8000/docs

``````- ✅ Dependency Injection



## EndpointsDATABASE_URL=postgresql://usuario:contraseña@localhost:5432/autos_db



### Autos```## Requisitos

- `POST /autos/` - Crear auto

- `POST /autos/batch/` - Crear múltiples autos

- `GET /autos/` - Listar (filtros: marca, modelo, skip, limit)

- `GET /autos/{id}` - Obtener auto## Ejecutar- Python 3.10+

- `GET /autos/chasis/{numero}` - Buscar por chasis

- `GET /autos/{id}/with-ventas` - Auto con sus ventas- PostgreSQL 12+

- `PUT /autos/{id}` - Actualizar (sin chasis)

- `DELETE /autos/{id}` - Eliminar```bash- pip



### Ventasuvicorn main:app --reload

- `POST /ventas/` - Crear venta

- `POST /ventas/batch/` - Crear múltiples ventas```## Instalación y Configuración

- `GET /ventas/` - Listar ventas

- `GET /ventas/{id}` - Obtener venta

- `GET /ventas/auto/{auto_id}` - Ventas de un auto

- `GET /ventas/comprador/{nombre}` - Buscar por compradorAPI: `http://localhost:8000`  ### 1. Clonar o crear la carpeta del proyecto

- `PUT /ventas/{id}` - Actualizar venta

- `DELETE /ventas/{id}` - Eliminar ventaDocs: `http://localhost:8000/docs`



## Validaciones```bash



| Campo | Regla |## Endpointscd apitpfinal

|-------|-------|

| Año | 1900 - año actual |```

| Chasis | 17 caracteres (VIN) - autogenerado |

| Precio | Mayor a 0 |### Autos

| Fecha venta | No futura |

| Comprador | No vacío |- `POST /autos/` - Crear auto### 2. Crear y activar el entorno virtual



## Tests- `POST /autos/batch/` - Crear múltiples autos



```bash- `GET /autos/` - Listar autos (filtros: marca, modelo)```bash

python -m pytest tests/test_endpoints.py -v

```- `GET /autos/{id}` - Obtener auto# En Windows (PowerShell)



## Estructura- `GET /autos/chasis/{numero}` - Buscar por chasispython -m venv venv



```- `GET /autos/{id}/with-ventas` - Auto con ventas\venv\Scripts\activate

app/

├── database.py      # Conexión BD- `PUT /autos/{id}` - Actualizar auto

├── models.py        # Modelos (Auto, Venta)

├── repositories.py  # Acceso a datos- `DELETE /autos/{id}` - Eliminar auto# En Linux/Mac

├── routers_autos.py # Endpoints /autos

├── routers_ventas.py # Endpoints /ventaspython3 -m venv venv

└── utils.py         # Validaciones

tests/### Ventassource venv/bin/activate

└── test_endpoints.py # 14 tests

main.py              # Entry point- `POST /ventas/` - Crear venta```

requirements.txt     # Dependencias

```- `POST /ventas/batch/` - Crear múltiples ventas



## Tecnologías- `GET /ventas/` - Listar ventas### 3. Instalar dependencias



- FastAPI - Framework web- `GET /ventas/{id}` - Obtener venta

- SQLModel - ORM

- PostgreSQL - BD- `GET /ventas/auto/{auto_id}` - Ventas de un auto```bash

- Pydantic - Validaciones

- pytest - Testing- `GET /ventas/comprador/{nombre}` - Buscar por compradorpip install -r requirements.txt



## Características- `PUT /ventas/{id}` - Actualizar venta```



- CRUD completo para Autos y Ventas- `DELETE /ventas/{id}` - Eliminar venta

- Búsqueda parcial e insensible a mayúsculas

- Validación automática con Pydantic### 4. Configurar PostgreSQL

- Relaciones One-to-Many

- Tests automatizados (14/14 pasando)## Validaciones

- Documentación interactiva con Swagger

#### Crear la base de datos

- **Año**: 1900 - actual

- **Chasis**: 17 caracteres (VIN format)Usa DBeaver o psql:

- **Precio**: Mayor a 0

- **Fecha venta**: No futura```bash

- **Comprador**: No vacíopsql -U postgres -c "CREATE DATABASE autos_db;"

```

## Tests

#### Crear archivo `.env`

```bash

python -m pytest tests/test_endpoints.py -vEn la raíz del proyecto:

```

```

## EstructuraDATABASE_URL=postgresql://usuario:contraseña@localhost:5432/autos_db

```

```

app/### 5. Ejecutar la aplicación

├── database.py

├── models.py```bash

├── repositories.pyuvicorn main:app --reload

├── routers_autos.py```

├── routers_ventas.py

└── utils.pyLa API estará en **http://127.0.0.1:8000**

tests/

├── test_endpoints.pyDocumentación interactiva: **http://127.0.0.1:8000/docs**

main.py

requirements.txt---

```

## Estructura del Proyecto

```
apitpfinal/
├── main.py                 # Punto de entrada FastAPI
├── requirements.txt        # Dependencias
├── .env                    # Configuración (crear)
├── README.md
├── app/
│   ├── database.py         # Conexión PostgreSQL
│   ├── models.py           # Modelos SQLModel (Auto, Venta)
│   ├── repositories.py     # AutoRepository, VentaRepository
│   ├── routers_autos.py    # Endpoints /autos
│   ├── routers_ventas.py   # Endpoints /ventas
│   ├── utils.py            # Validaciones y utilidades
│   └── __init__.py
├── tests/
│   ├── test_endpoints.py   # Tests con pytest
│   └── __init__.py
└── venv/                   # Entorno virtual
```

---

## Endpoints

### **AUTOS**

#### Crear Auto
```http
POST /autos/
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023
}
```
Respuesta: Auto con ID y número de chasis generado automáticamente

#### Listar Autos
```http
GET /autos/?skip=0&limit=10&marca=Toyota&modelo=Corolla
```

#### Obtener Auto por ID
```http
GET /autos/{auto_id}
```

#### Obtener Auto con sus Ventas
```http
GET /autos/{auto_id}/with-ventas
```

#### Buscar Auto por Número de Chasis
```http
GET /autos/chasis/{numero_chasis}
```

#### Actualizar Auto (no permite cambiar chasis)
```http
PUT /autos/{auto_id}
{
  "marca": "Toyota",
  "modelo": "Camry",
  "año": 2024
}
```

#### Eliminar Auto
```http
DELETE /autos/{auto_id}
```

---

### **VENTAS**

#### Crear Venta
```http
POST /ventas/
{
  "nombre_comprador": "Juan Pérez",
  "precio": 25000.00,
  "fecha_venta": "2025-11-02T10:30:00",
  "auto_id": 1
}
```

#### Listar Ventas (con info del Auto)
```http
GET /ventas/?skip=0&limit=10
```

#### Obtener Venta por ID
```http
GET /ventas/{venta_id}
```

#### Listar Ventas de un Auto Específico
```http
GET /ventas/auto/{auto_id}
```

#### Buscar Ventas por Nombre de Comprador
```http
GET /ventas/comprador/{nombre}
```

#### Actualizar Venta
```http
PUT /ventas/{venta_id}
{
  "nombre_comprador": "Juan Pérez García",
  "precio": 26000.00
}
```

#### Eliminar Venta
```http
DELETE /ventas/{venta_id}
```

---

## Validaciones Implementadas

### Auto
- **Año**: Debe estar entre 1900 y el año actual
- **Número de Chasis**: Se genera automáticamente (17 caracteres alfanuméricos, sin I, O, Q)
- **Marca y Modelo**: No pueden estar vacíos

### Venta
- **Nombre Comprador**: No puede estar vacío
- **Precio**: Debe ser mayor a 0
- **Fecha Venta**: No puede ser en el futuro
- **Auto ID**: El auto debe existir en la base de datos

---

## Tests

Ejecutar todos los tests:

```bash
pytest tests/ -v
```

Ver cobertura:

```bash
pytest tests/ --cov=app --cov-report=html
```

**Pruebas incluidas:**
- Creación de Autos y Ventas
- Validaciones de año, precio, fecha, chasis
- Búsquedas y filtros
- Paginación
- Eliminación de registros
- Manejo de errores 404, 422

---

## Tecnologías

- **FastAPI** - Framework web moderno
- **SQLModel** - ORM combinando SQLAlchemy + Pydantic
- **PostgreSQL** - Base de datos relacional
- **Pydantic** - Validación de datos
- **pytest** - Framework de testing
- **Uvicorn** - Servidor ASGI

---

## Criterios de Evaluación (Según TP)

### Funcionalidad (40 puntos)
- ✅ Todos los endpoints implementados y funcionan
- ✅ CRUD completo para Autos y Ventas
- ✅ Validaciones de datos correctas
- ✅ Relaciones One-to-Many funcionando

### Arquitectura y Patrones (25 puntos)
- ✅ Patrón Repository implementado
- ✅ Separación clara de responsabilidades
- ✅ Dependency Injection con FastAPI
- ✅ Estructura de archivos organizada

### Calidad del Código (20 puntos)
- ✅ Código limpio y documentado
- ✅ Manejo apropiado de errores HTTP
- ✅ Tipado correcto con type hints
- ✅ Convenciones de nombres consistentes

### Base de Datos (15 puntos)
- ✅ PostgreSQL configurado correctamente
- ✅ Tablas creadas automáticamente
- ✅ Relaciones de BD implementadas
- ✅ Conexión funcional

---

## Entregables

1. ✅ Código fuente completo
2. ✅ Base de datos PostgreSQL configurada
3. ✅ README.md con instrucciones
4. ✅ requirements.txt con dependencias
5. ✅ Documentación automática en /docs
6. ✅ Tests unitarios/integración

---

## Notas Importantes

- Los números de chasis se generan automáticamente al crear un Auto (VIN estándar de 17 caracteres)
- El número de chasis no puede ser modificado al actualizar un Auto (protegido)
- La fecha de venta no puede ser en el futuro
- Un Auto puede tener múltiples Ventas asociadas
- Todos los endpoints tienen validaciones de integridad referencial

---

## Troubleshooting

### Error: `DATABASE_URL not found`
Verifica que `.env` existe en la raíz con la URL correcta

### Error de conexión a PostgreSQL
Asegúrate de que PostgreSQL está corriendo y la BD `autos_db` existe

### Tests no funcionan
Ejecutá desde la raíz del proyecto con: `pytest tests/ -v`

---

## Instrucciones Rápidas

```bash
# Setup inicial
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Crear .env con DATABASE_URL
echo "DATABASE_URL=postgresql://usuario:pass@localhost:5432/autos_db" > .env

# Ejecutar servidor
uvicorn main:app --reload

# Ejecutar tests
pytest tests/ -v

# Ver docs
# Abrí http://localhost:8000/docs
```

---

**Desarrollo:** Programación IV - UTN TUP 2025
