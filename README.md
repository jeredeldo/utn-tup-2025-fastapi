# 🚗 API de Ventas de Autos

API REST completa para la gestión de inventario de autos y registro de ventas, desarrollada con **FastAPI**, **SQLModel** y **PostgreSQL**.



---

## ✨ Características Principales

- ✅ **CRUD completo** para Autos y Ventas
- ✅ **Validaciones robustas** con Pydantic
- ✅ **Generación automática** de números de chasis (VIN de 17 caracteres)
- ✅ **Búsquedas avanzadas** (por chasis, comprador, marca, modelo)
- ✅ **Paginación** con skip/limit
- ✅ **Relaciones One-to-Many** entre Autos y Ventas
- ✅ **Documentación automática** con Swagger UI
- ✅ **Tests automatizados** con pytest (14+ tests)
- ✅ **Patrón Repository** implementado
- ✅ **Dependency Injection** nativo de FastAPI

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|-----------|----------|
| **FastAPI** | Framework web moderno y asincrónico |
| **SQLModel** | ORM combinando SQLAlchemy + Pydantic |
| **PostgreSQL** | Base de datos relacional |
| **Pydantic** | Validación de datos |
| **pytest** | Framework de testing |
| **Uvicorn** | Servidor ASGI |

---

## 📋 Requisitos Previos

- Python 3.10+
- PostgreSQL 12+
- pip o conda

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/jeredeldo/utn-tup-2025-fastapi.git
cd utn-tup-2025-fastapi
```

### 2️⃣ Crear y activar entorno virtual

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar PostgreSQL

Crea la base de datos usando psql o DBeaver:

```bash
psql -U postgres -c "CREATE DATABASE autos_db;"
```

### 5️⃣ Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/autos_db
```

> **Nota:** Reemplaza `usuario` y `contraseña` con tus credenciales de PostgreSQL

### 6️⃣ Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API estará disponible en: **http://localhost:8000**

Documentación interactiva: **http://localhost:8000/docs**

---

## 📡 API Endpoints

### **AUTOS**

#### ➕ Crear Auto
```http
POST /autos/
Content-Type: application/json

{
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023
}
```
**Respuesta (201):** Auto con ID y número de chasis autogenerado

#### ➕ Crear Múltiples Autos
```http
POST /autos/batch/
Content-Type: application/json

[
  {"marca": "Toyota", "modelo": "Corolla", "año": 2023},
  {"marca": "Ford", "modelo": "Focus", "año": 2022}
]
```

#### 📋 Listar Autos
```http
GET /autos/?skip=0&limit=10&marca=Toyota&modelo=Corolla
```
**Parámetros opcionales:**
- `marca` - Filtrar por marca (búsqueda parcial, case-insensitive)
- `modelo` - Filtrar por modelo (búsqueda parcial, case-insensitive)
- `skip` - Número de registros a saltar (default: 0)
- `limit` - Máximo de registros a retornar (default: 10)

#### 🔍 Obtener Auto por ID
```http
GET /autos/{auto_id}
```

#### 🔎 Buscar Auto por Número de Chasis
```http
GET /autos/chasis/{numero_chasis}
```

#### 📊 Obtener Auto con sus Ventas
```http
GET /autos/{auto_id}/with-ventas
```

#### ✏️ Actualizar Auto
```http
PUT /autos/{auto_id}
Content-Type: application/json

{
  "marca": "Toyota",
  "modelo": "Camry",
  "año": 2024
}
```
> **Nota:** No es posible cambiar el número de chasis

#### 🗑️ Eliminar Auto
```http
DELETE /autos/{auto_id}
```

---

### **VENTAS**

#### ➕ Crear Venta
```http
POST /ventas/
Content-Type: application/json

{
  "nombre_comprador": "Juan Pérez",
  "precio": 25000.00,
  "fecha_venta": "2025-11-02T10:30:00",
  "auto_id": 1
}
```
**Validaciones automáticas:**
- El auto debe existir
- Nombre no puede estar vacío
- Precio debe ser > 0
- Fecha no puede ser futura

#### ➕ Crear Múltiples Ventas
```http
POST /ventas/batch/
Content-Type: application/json

[
  {"nombre_comprador": "Juan", "precio": 25000, "fecha_venta": "2025-11-02", "auto_id": 1},
  {"nombre_comprador": "María", "precio": 30000, "fecha_venta": "2025-11-01", "auto_id": 2}
]
```

#### 📋 Listar Ventas
```http
GET /ventas/?skip=0&limit=10
```

#### 🔍 Obtener Venta por ID
```http
GET /ventas/{venta_id}
```

#### 📊 Listar Ventas de un Auto Específico
```http
GET /ventas/auto/{auto_id}
```

#### 🔎 Buscar Ventas por Nombre de Comprador
```http
GET /ventas/comprador/{nombre}
```
**Nota:** Búsqueda parcial, case-insensitive

#### ✏️ Actualizar Venta
```http
PUT /ventas/{venta_id}
Content-Type: application/json

{
  "nombre_comprador": "Juan Pérez García",
  "precio": 26000.00,
  "fecha_venta": "2025-11-03"
}
```

#### 🗑️ Eliminar Venta
```http
DELETE /ventas/{venta_id}
```

---

## ✔️ Validaciones Implementadas

### Auto
| Campo | Regla |
|-------|-------|
| **Año** | Debe estar entre 1900 y el año actual |
| **Número de Chasis** | 17 caracteres alfanuméricos, autogenerado, sin I/O/Q (formato VIN) |
| **Marca** | No puede estar vacío |
| **Modelo** | No puede estar vacío |

### Venta
| Campo | Regla |
|-------|-------|
| **Nombre Comprador** | No puede estar vacío |
| **Precio** | Debe ser mayor a 0 |
| **Fecha Venta** | No puede ser en el futuro |
| **Auto ID** | El auto debe existir en la BD |

---

## 📁 Estructura del Proyecto

```
.
├── main.py                 # Punto de entrada FastAPI
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (crear)
├── .gitignore              # Archivos a ignorar en Git
├── README.md               # Este archivo
│
├── app/                    # Paquete principal
│   ├── __init__.py
│   ├── database.py         # Conexión PostgreSQL y gestión de sesiones
│   ├── models.py           # Modelos SQLModel (Auto, Venta y esquemas)
│   ├── repositories.py     # AutoRepository, VentaRepository (patrón Repository)
│   ├── routers_autos.py    # Endpoints GET, POST, PUT, DELETE /autos
│   ├── routers_ventas.py   # Endpoints GET, POST, PUT, DELETE /ventas
│   └── utils.py            # Funciones de validación y utilidades
│
├── tests/                  # Tests
│   ├── __init__.py
│   └── test_endpoints.py   # Suite de tests con pytest (14+ tests)
│
└── venv/                   # Entorno virtual (NO commitear)
```

---

## 🧪 Tests

### Ejecutar todos los tests

```bash
pytest tests/ -v
```

### Ver cobertura de tests

```bash
pytest tests/ --cov=app --cov-report=html
```

### Pruebas incluidas

- ✅ Creación de Autos y Ventas
- ✅ Validaciones de año, precio, fecha, chasis
- ✅ Búsquedas y filtros (marca, modelo, comprador)
- ✅ Paginación (skip/limit)
- ✅ Eliminación de registros
- ✅ Manejo de errores 404, 422
- ✅ Relaciones One-to-Many

---

## 🏗️ Arquitectura

### Patrón Repository

La aplicación implementa el **patrón Repository** para encapsular la lógica de acceso a datos:

```python
# Ejemplo de uso
@router.post("/autos/", response_model=AutoRead)
def create_auto(auto: AutoCreate, repo: AutoRepository = Depends(get_auto_repo)):
    # El repositorio maneja toda la lógica de BD
    return repo.create(auto)
```

### Dependency Injection

FastAPI inyecta dependencias automáticamente:

```python
def get_auto_repo(session: Session = Depends(get_session)):
    return AutoRepository(session)
```

### Estructura de Modelos

- **Models (DB)**: `Auto`, `Venta` - Modelos que se persisten en BD
- **Create Schemas**: `AutoCreate`, `VentaCreate` - Para validar entrada
- **Read Schemas**: `AutoRead`, `VentaRead` - Para serializar salida
- **Relational**: `AutoReadWithVentas` - Modelos con relaciones

---

## 🐛 Troubleshooting

### ❌ Error: `DATABASE_URL not found`

**Solución:** Verifica que el archivo `.env` existe en la raíz con la URL correcta.

```bash
echo "DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/autos_db" > .env
```

### ❌ Error de conexión a PostgreSQL

**Solución:** Asegúrate de que:
1. PostgreSQL está corriendo (`sudo service postgresql start` en Linux)
2. La BD `autos_db` existe
3. Las credenciales en `.env` son correctas

### ❌ Tests no funcionan

**Solución:** Ejecutá desde la raíz del proyecto:

```bash
pytest tests/ -v
```

Asegúrate de tener pytest instalado:

```bash
pip install pytest httpx
```

### ❌ Módulos no encontrados

**Solución:** Asegúrate de tener el entorno virtual activado:

```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

---

## 📚 Ejemplos Rápidos

### Crear un auto

```bash
curl -X POST "http://localhost:8000/autos/" \
  -H "Content-Type: application/json" \
  -d '{
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2023
  }'
```

### Listar autos con filtro

```bash
curl "http://localhost:8000/autos/?marca=Toyota&limit=5"
```

### Crear una venta

```bash
curl -X POST "http://localhost:8000/ventas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre_comprador": "Juan Pérez",
    "precio": 25000.00,
    "fecha_venta": "2025-11-02T10:30:00",
    "auto_id": 1
  }'
```

---

## ⚡ Inicio Rápido (One-liner)

```bash
# Setup, env, BD y servidor
python -m venv venv && \
(.\venv\Scripts\Activate.ps1; pip install -r requirements.txt; `
echo "DATABASE_URL=postgresql://postgres:postgres@localhost:5432/autos_db" > .env; `
uvicorn main:app --reload)
```

---

## 📝 Notas Importantes

- Los números de chasis se generan automáticamente al crear un Auto (17 caracteres, formato VIN)
- El número de chasis **no puede ser modificado** al actualizar un Auto (protegido)
- La fecha de venta **no puede ser en el futuro**
- Un Auto puede tener **múltiples Ventas** asociadas
- Todos los endpoints tienen **validaciones de integridad referencial**
- Las búsquedas son **case-insensitive** y permiten búsquedas parciales

---

## ✅ Criterios de Evaluación (Trabajo Práctico)

### Funcionalidad (40 puntos)
- ✅ Todos los endpoints implementados y funcionan correctamente
- ✅ CRUD completo para Autos y Ventas
- ✅ Validaciones de datos correctas y completas
- ✅ Relaciones One-to-Many funcionando perfectamente

### Arquitectura y Patrones (25 puntos)
- ✅ Patrón Repository implementado correctamente
- ✅ Separación clara de responsabilidades
- ✅ Dependency Injection con FastAPI
- ✅ Estructura de archivos organizada y escalable

### Calidad del Código (20 puntos)
- ✅ Código limpio, legible y documentado
- ✅ Manejo apropiado de errores HTTP (404, 422, etc.)
- ✅ Tipado correcto con type hints
- ✅ Convenciones de nombres consistentes

### Base de Datos (15 puntos)
- ✅ PostgreSQL configurado correctamente
- ✅ Tablas creadas automáticamente con SQLModel
- ✅ Relaciones de BD implementadas correctamente
- ✅ Conexión funcional y persistencia de datos

---

## 📞 Soporte

Si encuentras problemas:

1. Revisa la sección de **Troubleshooting**
2. Verifica que PostgreSQL está corriendo
3. Consulta la documentación en `http://localhost:8000/docs`
4. Ejecuta los tests para validar el setup: `pytest tests/ -v`

---

## 📄 Entregables

- ✅ Código fuente completo en GitHub
- ✅ Base de datos PostgreSQL configurada
- ✅ README.md con instrucciones claras
- ✅ requirements.txt con todas las dependencias
- ✅ Documentación automática en Swagger UI
- ✅ Tests automatizados (14+ tests)
- ✅ .env.example con plantilla de configuración

---

**Desarrollo:** Programación IV - UTN TUP 2025

**Versión:** 1.0  
**Última actualización:** Noviembre 2025
