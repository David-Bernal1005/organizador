import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Asegurar que el módulo backend está en el path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(
    title="API Organizador de Tareas",
    version="1.0.0",
    description="API para gestionar tareas y usuarios"
)

# Configurar CORS con múltiples orígenes permitidos
ALLOWED_ORIGINS_STR = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"
)

ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS_STR.split(",") if origin.strip()]

# En producción, agregar orígenes de Vercel
if "onrender.com" in os.getenv("DATABASE_URL", ""):
    VERCEL_ORIGINS = [
        "https://organizador.vercel.app",
        "https://organizador-cyan.vercel.app",
    ]
    ALLOWED_ORIGINS.extend(VERCEL_ORIGINS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints básicos
@app.get("/")
def inicio():
    return {"mensaje": "API funcionando", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "allowed_origins": ALLOWED_ORIGINS
    }

# Importar routers DESPUÉS de crear la app
try:
    from backend.app.api.endpoint.auth import router as auth_router
    from backend.app.api.endpoint.tarea import router as tarea_router
    
    app.include_router(auth_router, prefix="/api")
    app.include_router(tarea_router, prefix="/api")
except Exception as e:
    print(f"⚠️  Advertencia: No se pudieron cargar los routers: {e}")
    print("La API estará disponible pero sin los endpoints de auth y tareas")
    import traceback
    traceback.print_exc()

