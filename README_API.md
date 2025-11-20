# Referencia de API

## URL Base

```
http://localhost:8000/api/v1
```

## Autenticación

Actualmente no se requiere autenticación. Implementar JWT tokens para producción.

---

## Vehículos (Autos)

### Crear Vehículo

**Endpoint**: `POST /autos/`

**Cuerpo de la Solicitud**:
```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023
}
```

**Respuesta** (201 Creado):
```json
{
  "id": 1,
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023,
  "numero_chasis": "1HGBH41JXMN109186"
}
```

### Crear Múltiples Vehículos

**Endpoint**: `POST /autos/batch/`

**Cuerpo de la Solicitud**:
```json
[
  {"marca": "Toyota", "modelo": "Corolla", "año": 2023},
  {"marca": "Ford", "modelo": "Focus", "año": 2022}
]
```

### Listar Vehículos

**Endpoint**: `GET /autos/`

**Parámetros de Consulta**:
- `skip` (int, default: 0) - Registros a omitir
- `limit` (int, default: 10) - Registros a devolver
- `marca` (string, opcional) - Filtrar por marca
- `modelo` (string, opcional) - Filtrar por modelo

**Ejemplo**:
```
GET /autos/?marca=Toyota&limit=5
```

**Respuesta** (200 OK):
```json
[
  {
    "id": 1,
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2023,
    "numero_chasis": "1HGBH41JXMN109186"
  }
]
```

### Obtener Vehículo por ID

**Endpoint**: `GET /autos/{auto_id}`

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023,
  "numero_chasis": "1HGBH41JXMN109186"
}
```

### Obtener Vehículo por VIN

**Endpoint**: `GET /autos/chasis/{numero_chasis}`

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "marca": "Toyota",
  "modelo": "Corolla",
  "año": 2023,
  "numero_chasis": "1HGBH41JXMN109186"
}
```

### Actualizar Vehículo

**Endpoint**: `PUT /autos/{auto_id}`

**Cuerpo de la Solicitud**:
```json
{
  "marca": "Toyota",
  "modelo": "Camry",
  "año": 2024
}
```

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "marca": "Toyota",
  "modelo": "Camry",
  "año": 2024,
  "numero_chasis": "1HGBH41JXMN109186"
}
```

### Eliminar Vehículo

**Endpoint**: `DELETE /autos/{auto_id}`

**Respuesta**: 204 Sin Contenido

---

## Ventas (Ventas)

### Crear Venta

**Endpoint**: `POST /ventas/`

**Cuerpo de la Solicitud**:
```json
{
  "auto_id": 1,
  "nombre_comprador": "Juan Pérez",
  "precio": 25000.00,
  "fecha_venta": "2024-11-19T10:30:00"
}
```

**Respuesta** (201 Creado):
```json
{
  "id": 1,
  "auto_id": 1,
  "nombre_comprador": "Juan Pérez",
  "precio": 25000.00,
  "fecha_venta": "2024-11-19T10:30:00",
  "auto": {
    "id": 1,
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2023,
    "numero_chasis": "1HGBH41JXMN109186"
  }
}
```

### Crear Múltiples Ventas

**Endpoint**: `POST /ventas/batch/`

**Cuerpo de la Solicitud**:
```json
[
  {
    "auto_id": 1,
    "nombre_comprador": "Juan Pérez",
    "precio": 25000.00,
    "fecha_venta": "2024-11-19T10:30:00"
  },
  {
    "auto_id": 2,
    "nombre_comprador": "María García",
    "precio": 30000.00,
    "fecha_venta": "2024-11-18T15:00:00"
  }
]
```

### Listar Ventas

**Endpoint**: `GET /ventas/`

**Parámetros de Consulta**:
- `skip` (int, default: 0) - Registros a omitir
- `limit` (int, default: 10) - Registros a devolver

**Respuesta** (200 OK):
```json
[
  {
    "id": 1,
    "auto_id": 1,
    "nombre_comprador": "Juan Pérez",
    "precio": 25000.00,
    "fecha_venta": "2024-11-19T10:30:00",
    "auto": {
      "id": 1,
      "marca": "Toyota",
      "modelo": "Corolla",
      "año": 2023,
      "numero_chasis": "1HGBH41JXMN109186"
    }
  }
]
```

### Obtener Venta por ID

**Endpoint**: `GET /ventas/{venta_id}`

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "auto_id": 1,
  "nombre_comprador": "Juan Pérez",
  "precio": 25000.00,
  "fecha_venta": "2024-11-19T10:30:00",
  "auto": {
    "id": 1,
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2023,
    "numero_chasis": "1HGBH41JXMN109186"
  }
}
```

### Obtener Ventas por Vehículo

**Endpoint**: `GET /ventas/auto/{auto_id}`

**Respuesta** (200 OK):
```json
[
  {
    "id": 1,
    "auto_id": 1,
    "nombre_comprador": "Juan Pérez",
    "precio": 25000.00,
    "fecha_venta": "2024-11-19T10:30:00",
    "auto": {
      "id": 1,
      "marca": "Toyota",
      "modelo": "Corolla",
      "año": 2023,
      "numero_chasis": "1HGBH41JXMN109186"
    }
  }
]
```

### Obtener Ventas por Nombre del Comprador

**Endpoint**: `GET /ventas/comprador/{nombre}`

**Respuesta** (200 OK):
```json
[
  {
    "id": 1,
    "auto_id": 1,
    "nombre_comprador": "Juan Pérez",
    "precio": 25000.00,
    "fecha_venta": "2024-11-19T10:30:00",
    "auto": {
      "id": 1,
      "marca": "Toyota",
      "modelo": "Corolla",
      "año": 2023,
      "numero_chasis": "1HGBH41JXMN109186"
    }
  }
]
```

### Actualizar Venta

**Endpoint**: `PUT /ventas/{venta_id}`

**Cuerpo de la Solicitud**:
```json
{
  "nombre_comprador": "Juan Pérez García",
  "precio": 26000.00,
  "fecha_venta": "2024-11-20T11:00:00"
}
```

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "auto_id": 1,
  "nombre_comprador": "Juan Pérez García",
  "precio": 26000.00,
  "fecha_venta": "2024-11-20T11:00:00"
}
```

### Eliminar Venta

**Endpoint**: `DELETE /ventas/{venta_id}`

**Respuesta**: 204 Sin Contenido

---

## Respuestas de Error

### Solicitud Inválida (400)
```json
{
  "detail": "El año debe estar entre 1900 y el año actual."
}
```

### No Encontrado (404)
```json
{
  "detail": "Vehículo no encontrado."
}
```

### Error de Validación (422)
```json
{
  "detail": [
    {
      "loc": ["body", "año"],
      "msg": "asegurate de que este valor es menor o igual a 2024",
      "type": "value_error.number.not_le"
    }
  ]
}
```

---

## Códigos de Estado

| Código | Descripción |
|------|-------------|
| 200 | OK |
| 201 | Creado |
| 204 | Sin Contenido |
| 400 | Solicitud Inválida |
| 404 | No Encontrado |
| 422 | Entidad No Procesable |
| 500 | Error Interno del Servidor |

---

## Reglas de Validación

### Vehículo
- `año`: 1900 al año actual
- `marca`: String no vacío
- `modelo`: String no vacío
- `numero_chasis`: Auto-generado, único, formato VIN de 17 caracteres

### Venta
- `nombre_comprador`: String no vacío
- `precio`: Mayor a 0
- `fecha_venta`: No en el futuro
- `auto_id`: Debe referenciar un vehículo existente

---

## Limitación de Velocidad

Actualmente no implementado. Agregar para uso en producción.

---

**Última Actualización**: Noviembre 2024
