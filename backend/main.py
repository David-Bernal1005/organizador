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

# Configurar CORS - Leer orígenes permitidos de variable de entorno
# Por defecto permite localhost + todo *.vercel.app
ALLOWED_ORIGINS_STR = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"
)

ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS_STR.split(",") if origin.strip()]

# En producción (Render), añadir dominios Vercel genéricos
if "onrender.com" in os.getenv("DATABASE_URL", ""):
    # Estos son patrones comunes de Vercel
    ALLOWED_ORIGINS.extend([
        "https://organizador.vercel.app",
        "https://organizador-cyan.vercel.app",
        # Los preview deployments son dinámicos (ej. organizador-gp4lcevur-...vercel.app)
        # Así que permitimos el patrón completo en la URL con regex
    ])

# Usar allow_origin_regex para aceptar dinámicamente previews de Vercel y servicios en Render
# Patrón: https://organizador-*.vercel.app, https://cualquier-cosa.onrender.com, localhost
ALLOW_ORIGIN_REGEX = r"https://.*\.vercel\.app$|https://.*\.onrender\.com$|https://localhost.*|http://127\.0\.0\.1.*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # Orígenes explícitos
    allow_origin_regex=ALLOW_ORIGIN_REGEX,  # Patrón para previews dinámicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints básicos
@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "allowed_origins": ALLOWED_ORIGINS,
        "allow_origin_regex": ALLOW_ORIGIN_REGEX
    }

# Importar routers DESPUÉS de crear la app
try:
    from backend.app.api.endpoint.auth import router as auth_router
    from backend.app.api.endpoint.tarea import router as tarea_router
    
    app.include_router(auth_router, prefix="/api")
    app.include_router(tarea_router, prefix="/api")
    print("✓ Routers cargados exitosamente")
except Exception as e:
    print(f"⚠️  Advertencia: No se pudieron cargar los routers: {e}")
    print("La API estará disponible pero sin los endpoints de auth y tareas")
    import traceback
    traceback.print_exc()

