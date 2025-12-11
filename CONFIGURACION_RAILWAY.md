# Conexión a Base de Datos Railway - Guía de Configuración

## ✓ Cambios Realizados

### 1. **Configuración Actualizada**
- ✅ `backend/app/core/config.py` - URL de Railway configurada
- ✅ `backend/app/db/session.py` - Engine mejorado con opciones de pool
- ✅ `requirements.txt` - Agregado `pymysql` en lugar de `psycopg2`
- ✅ `.env` - Archivo de variables de entorno creado

### 2. **Dependencias Instaladas**
```
pymysql              # Driver para MySQL/MariaDB
cryptography         # Autenticación SHA2
python-dotenv        # Gestión de variables de entorno
SQLAlchemy           # ORM
```

### 3. **Base de Datos Conectada**
- URL: `mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway`
- Estado: ✅ Conexión exitosa verificada

## 📋 Próximos Pasos

### 1. Crear las tablas en la base de datos
```bash
python create_tables.py
```

### 2. Ejecutar el servidor FastAPI
```bash
cd backend
uvicorn app.main:app --reload
```

### 3. Usar en tu aplicación
Las conexiones se manejan automáticamente mediante:
```python
from backend.app.db.session import get_db
from fastapi import Depends

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    # db es la sesión de la base de datos
    items = db.query(Usuario).all()
    return items
```

## ⚠️ Seguridad en Producción

**IMPORTANTE:** Por seguridad, la URL de la base de datos está en el archivo `.env`.

Si desplegaste en producción:
1. **NO** subas el archivo `.env` a Git
2. Añade `.env` a `.gitignore` (si no está ya)
3. Configura las variables de entorno en tu plataforma de hosting (Railway, Vercel, etc.)

### Ejemplo para Railway:
En el dashboard de Railway, configura:
```
DATABASE_URL=mysql+pymysql://...
SECRET_KEY=tu_clave_secreta
```

## 📚 Referencia de Modelos

Tus modelos SQLAlchemy están listos:

### Usuario
```python
class Usuario(Base):
    __tablename__ = "usuarios"
    id: Integer (Primary Key)
    nombre: String(120)
    correo: String(255) - UNIQUE
    contraseña: String(500)
    tareas: relationship con Tarea
```

### Tarea
```python
class Tarea(Base):
    __tablename__ = "tareas"
    id: Integer (Primary Key)
    titulo: String(255)
    descripcion: Text
    estado: Boolean (False=pendiente, True=completada)
    fecha_creacion: DateTime
    usuario_id: ForeignKey a usuarios.id
    usuario: relationship con Usuario
```

## ✨ Características de la Configuración

- **Pool Pre-Ping**: Verifica la conexión antes de usarla
- **Pool Recycle**: Recicla conexiones cada hora (importante para conexiones remotas)
- **Echo Deshabilitado**: No muestra queries en logs (mejor rendimiento)
- **Variables de Entorno**: Seguridad mejorada

¡Tu aplicación está lista para usar la base de datos de Railway! 🚀
