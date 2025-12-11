import os
from fastapi import FastAPI
from backend.app.api.endpoint.auth import router as auth_router
from backend.app.api.endpoint.tarea import router as tarea_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Organizador de Tareas", version="1.0.0")

# Configurar CORS con múltiples orígenes permitidos
# Leer de variable de entorno o usar valores por defecto
ALLOWED_ORIGINS_STR = os.getenv(
    "ALLOWED_ORIGINS",
    # Orígenes por defecto: localhost, vercel, y desarrollo local
    "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"
)

# Convertir string a lista, removiendo espacios
ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS_STR.split(",") if origin.strip()]

# En producción, agregar orígenes de Vercel
if "onrender.com" in os.getenv("DATABASE_URL", ""):
    # Si estamos en Render (producción), agregar orígenes comunes de Vercel
    VERCEL_ORIGINS = [
        "https://organizador.vercel.app",
        "https://organizador-cyan.vercel.app",
        "https://organizador-*.vercel.app",  # Wildcard para preview deployments
    ]
    ALLOWED_ORIGINS.extend(VERCEL_ORIGINS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers con prefijo /api
app.include_router(auth_router, prefix="/api")
app.include_router(tarea_router, prefix="/api")

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.get("/health")
def health_check():
    """Endpoint para verificar que la API está en línea"""
    return {
        "status": "ok",
        "allowed_origins": ALLOWED_ORIGINS
    }
