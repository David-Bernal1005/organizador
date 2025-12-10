from fastapi import FastAPI
from backend.app.api.endpoint.auth import router as auth_router

from backend.app.api.endpoint.tarea import router as tarea_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Organizador de Tareas", version="1.0.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
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
