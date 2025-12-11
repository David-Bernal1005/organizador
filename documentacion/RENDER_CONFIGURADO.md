# Backend Configurado para Render ✅

## 📁 Archivos Creados/Actualizados para Render

| Archivo | Propósito |
|---------|-----------|
| `build.sh` | Script de construcción que ejecuta Render |
| `Procfile` | Define cómo iniciar la aplicación |
| `render.yaml` | Configuración completa de Render (alternativa) |
| `.env.example` | Plantilla de variables de entorno |
| `GUIA_RENDER.md` | Instrucciones detalladas de despliegue |
| `backend/main.py` | Actualizado con CORS configurables |
| `create_tables.py` | Mejorado para manejar timeouts |

## 🚀 Pasos para Desplegar Ahora

### 1️⃣ En Render Dashboard

```
1. Accede a https://dashboard.render.com
2. Click en "New +" → "Web Service"
3. Selecciona tu repositorio: David-Bernal1005/organizador
4. Completa:
   - Name: api-organizador-tareas
   - Region: Oregon (free tier)
   - Branch: master
   - Runtime: Python 3
   - Build Command: bash ./build.sh
   - Start Command: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
```

### 2️⃣ Configurar Variables de Entorno

En el formulario de Render, sección "Environment":

```
DATABASE_URL
mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway

SECRET_KEY
generate-a-random-secret-key-here

ALLOWED_ORIGINS
http://localhost:5173,http://localhost:3000
(actualiza después con tu dominio de frontend)
```

### 3️⃣ Crear el Servicio

- Click en "Create Web Service"
- Espera a que se construya (2-5 minutos)
- Verifica que pasó el build

### 4️⃣ Probar la API

```bash
# Reemplaza con tu URL de Render
curl https://api-organizador-tareas.onrender.com/
# Debería devolver: {"mensaje": "API funcionando"}
```

## 🔍 Estructura del Proyecto para Render

```
c:\Users\USUARIO\organizador/
├── build.sh                 ← Script de build
├── Procfile                 ← Comando de inicio
├── render.yaml              ← Configuración alternativa
├── requirements.txt         ← Dependencias Python
├── create_tables.py         ← Crear tablas en DB
├── .env.example             ← Template de variables
├── backend/
│   ├── main.py             ← CORS configurables
│   └── app/
│       ├── api/
│       │   └── endpoint/
│       │       ├── auth.py
│       │       └── tarea.py
│       ├── models/
│       │   ├── usuario.py
│       │   └── tarea.py
│       ├── schemas/
│       ├── core/
│       │   └── config.py    ← Lee DATABASE_URL
│       └── db/
│           └── session.py   ← Configura engine
└── GUIA_RENDER.md          ← Instrucciones detalladas
```

## ✨ Cambios Clave Realizados

### 1. CORS Configurable
```python
# Ahora lee de variable de entorno
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
```

### 2. Script de Build Robusto
```bash
# build.sh instala dependencias y crea tablas
pip install -r requirements.txt
python create_tables.py
```

### 3. Reconexión Automática
```python
# En session.py
engine = create_engine(
    settings.DATABASE_URL, 
    pool_pre_ping=True,      # Verifica conexión
    pool_recycle=3600        # Recicla cada hora
)
```

### 4. Create Tables Mejorado
- Espera a que la BD esté disponible
- Maneja timeouts correctamente
- Retorna exit code apropiado

## 🔗 URLs Después del Despliegue

```
API:      https://api-organizador-tareas.onrender.com
Frontend: (tu URL de Vercel/Netlify/etc)

Actualiza tu frontend con:
const API_URL = "https://api-organizador-tareas.onrender.com/api"
```

## 📊 Monitoreo en Render

Después de desplegar, en el dashboard:
- **Logs** → Ver lo que sucede durante el build y ejecución
- **Metrics** → Ver CPU, memoria, requests
- **Events** → Historial de deployments
- **Settings** → Cambiar variables de entorno sin redeployar

## 🆘 Si Algo Falla

### Build failed
- Revisa los logs en Render
- `create_tables.py` intenta esperada hasta 10 segundos a la BD
- Si sigue fallando, ejecuta manualmente: `python create_tables.py`

### Connection timeout
- Verifica DATABASE_URL es correcto
- Asegúrate que Railway permite conexiones externas
- Usa `pool_pre_ping=True` (ya configurado)

### Module not found
- Verifica `requirements.txt` tiene todas las dependencias
- Revisa que el `build.sh` se ejecutó correctamente

## 💡 Siguientes Pasos

1. **Deploy en Render** siguiendo los pasos anteriores
2. **Conecta tu frontend** a la URL de Render
3. **Actualiza ALLOWED_ORIGINS** con el dominio de tu frontend
4. **Monitorea los logs** durante las primeras 24 horas

## 📞 Soporte

- [Documentación Render](https://render.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- Revisa `GUIA_RENDER.md` para instrucciones detalladas

---

**¡Tu backend está listo para Render!** 🎉

Solo falta seguir los 4 pasos en el Render Dashboard y tu API estará en vivo.
