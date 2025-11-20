# Guía de Configuración de PostgreSQL con Docker

## Descripción General

Esta guía proporciona instrucciones para configurar PostgreSQL usando Docker para el desarrollo local de la API de Gestión de Ventas de Vehículos. Docker asegura entornos de base de datos consistentes en todas las máquinas de desarrollo.

## Requisitos Previos

- Docker ([Instalar Docker](https://docs.docker.com/get-docker/))
- Docker Compose ([Instalar Docker Compose](https://docs.docker.com/compose/install/))
- Git

## Archivos Incluidos

| Archivo | Propósito |
|---------|---------|
| `Dockerfile.postgres` | Imagen personalizada de PostgreSQL con base de datos UTN preconfigurada |
| `docker-compose.yml` | Archivo de orquestación para fácil gestión de contenedores |
| `.env.example` | Plantilla de variables de entorno |

## Inicio Rápido

### Opción 1: Docker Compose (Recomendado)

1. **Iniciar Contenedor de PostgreSQL**
   ```bash
   docker-compose up -d postgres_utn
   ```

2. **Verificar que el Contenedor está Ejecutándose**
   ```bash
   docker-compose logs postgres_utn
   ```

3. **Detener Contenedor**
   ```bash
   docker-compose down
   ```

### Opción 2: Docker CLI

1. **Construir Imagen Personalizada**
   ```bash
   docker build -f Dockerfile.postgres -t postgres-utn .
   ```

2. **Ejecutar Contenedor**
   ```bash
   docker run -d \
     --name postgres_utn_db \
     -e POSTGRES_DB=UTN \
     -e POSTGRES_USER=postgres \
     -e POSTGRES_PASSWORD=postgres \
     -p 55432:5432 \
     -v postgres_utn_data:/var/lib/postgresql/data \
     postgres-utn
   ```

3. **Ver Logs**
   ```bash
   docker logs postgres_utn_db
   ```

4. **Detener Contenedor**
   ```bash
   docker stop postgres_utn_db
   docker rm postgres_utn_db
   ```

## Conexión a la Base de Datos

### Detalles de Conexión

| Parámetro | Valor |
|-----------|-------|
| Host | localhost |
| Puerto | 55432 |
| Base de Datos | UTN |
| Usuario | postgres |
| Contraseña | postgres |
| Cadena de Conexión | `postgresql://postgres:postgres@localhost:55432/UTN` |

### Configuración de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:55432/UTN
DEBUG=false
PORT=8000
HOST=0.0.0.0
```

O copiar desde la plantilla:
```bash
cp .env.example .env
```

## Conectar desde FastAPI

Actualizar tu archivo `config.py` o `.env` con la cadena de conexión:

```python
# config.py
import os
from sqlalchemy.engine import URL

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:55432/UTN"
)

# Crear motor
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
```

## Comandos Útiles

### Gestión de Contenedores

```bash
# Ver contenedores en ejecución
docker-compose ps

# Ver todos los contenedores
docker ps -a

# Ver logs del contenedor
docker-compose logs postgres_utn

# Seguir logs en tiempo real
docker-compose logs -f postgres_utn

# Acceder a CLI de PostgreSQL dentro del contenedor
docker exec -it postgres_utn_db psql -U postgres -d UTN
```

### Operaciones de Base de Datos

```bash
# Conectar a base de datos desde el host
psql -U postgres -h localhost -p 55432 -d UTN

# Listar todas las bases de datos
\l

# Conectar a base de datos específica
\c UTN

# Listar todas las tablas
\dt

# Describir estructura de tabla
\d nombre_tabla

# Salir de psql
\q
```

## Solución de Problemas

### Puerto Ya en Uso

Si el puerto 55432 ya está en uso:

1. **Modificar `docker-compose.yml`**
   ```yaml
   postgres_utn:
     ports:
       - "55433:5432"  # Cambiar primer puerto a 55433
   ```

2. **Actualizar `DATABASE_URL` en `.env`**
   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:55433/UTN
   ```

### El Contenedor No Inicia

1. **Verificar logs para errores**
   ```bash
   docker-compose logs postgres_utn
   ```

2. **Eliminar volúmenes huérfanos**
   ```bash
   docker volume prune
   ```

3. **Reconstruir imagen**
   ```bash
   docker-compose down
   docker-compose up -d --build postgres_utn
   ```

### Conexión Rechazada

1. **Verificar que el contenedor está ejecutándose**
   ```bash
   docker-compose ps
   ```

2. **Verificar que las credenciales coincidan** en el archivo `.env`

3. **Verificar mapeo de puertos**
   ```bash
   docker port postgres_utn_db
   ```

4. **Probar conexión**
   ```bash
   docker exec postgres_utn_db pg_isready -U postgres
   ```

### Permiso Denegado

```bash
# En Linux, agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker
```

## Persistencia de Volumen

Los datos se almacenan en el volumen de Docker `postgres_utn_data`, asegurando persistencia entre reinicios de contenedor:

```bash
# Listar todos los volúmenes
docker volume ls

# Inspeccionar volumen
docker volume inspect back_postgres_utn_data

# Ver ubicación del volumen
docker volume inspect back_postgres_utn_data --format='{{.Mountpoint}}'

# Eliminar volumen (ADVERTENCIA: Elimina todos los datos)
docker volume rm back_postgres_utn_data

# Limpiar volúmenes no utilizados
docker volume prune
```

## Copia de Seguridad y Restauración

### Realizar Copia de Seguridad de la Base de Datos

Crear un dump SQL de la base de datos:

```bash
docker exec postgres_utn_db pg_dump -U postgres UTN > backup.sql
```

O con compresión:
```bash
docker exec postgres_utn_db pg_dump -U postgres -F c UTN > backup.dump
```

### Restaurar Base de Datos

Desde dump SQL:
```bash
docker exec -i postgres_utn_db psql -U postgres UTN < backup.sql
```

Desde dump comprimido:
```bash
docker exec -i postgres_utn_db pg_restore -U postgres -d UTN -F c < backup.dump
```

## Optimización del Desempeño

### Agrupación de Conexiones

Para producción, configurar agrupación de conexiones en `docker-compose.yml`:

```yaml
postgres_utn:
  environment:
    POSTGRES_INITDB_ARGS: "-c max_connections=200"
```

### Configuración de Memoria

```yaml
postgres_utn:
  environment:
    POSTGRES_INITDB_ARGS: "-c shared_buffers=256MB -c effective_cache_size=1GB"
```

## Consideraciones para Producción

Para implementaciones en producción, implementar:

1. **Seguridad**
   - Usar contraseñas fuertes generadas aleatoriamente
   - Cambiar credenciales predeterminadas
   - Usar gestión de secretos de entorno
   - Habilitar conexiones SSL/TLS

2. **Monitoreo**
   - Configurar recopilación y agregación de logs
   - Monitorear métricas de desempeño de la base de datos
   - Configurar alertas para problemas críticos
   - Rastrear tiempos de ejecución de consultas

3. **Estrategia de Copia de Seguridad**
   - Copias de seguridad automatizadas regulares
   - Probar procedimientos de restauración periódicamente
   - Almacenar copias de seguridad en múltiples ubicaciones
   - Usar políticas de retención de copias de seguridad

4. **Desempeño**
   - Configurar configuración de memoria apropiada
   - Agregar índices a columnas frecuentemente consultadas
   - Monitorear y optimizar consultas lentas
   - Usar agrupación de conexiones

## Patrones Comunes de Docker Compose

### Configuración de Desarrollo

```yaml
version: '3.8'
services:
  postgres_utn:
    image: postgres:15-alpine
    container_name: postgres_utn_db
    environment:
      POSTGRES_DB: UTN
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "55432:5432"
    volumes:
      - postgres_utn_data:/var/lib/postgresql/data
    networks:
      - car-sales-network

volumes:
  postgres_utn_data:

networks:
  car-sales-network:
    driver: bridge
```

### Configuración Multi-Servicio

Para FastAPI + PostgreSQL en un archivo compose:

```yaml
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: UTN
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/UTN
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
```

## Recursos

- [Documentación de Docker](https://docs.docker.com/)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)
- [Documentación de PostgreSQL](https://www.postgresql.org/docs/)
- [Imagen Oficial de PostgreSQL Docker](https://hub.docker.com/_/postgres)
- [Referencia de CLI de PostgreSQL](https://www.postgresql.org/docs/current/app-psql.html)

---

**Versión**: 1.0  
**Última Actualización**: Noviembre 2024  
**Responsable**: Equipo de Desarrollo
