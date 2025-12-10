from sqlalchemy.orm import declarative_base

# Base para todos los modelos SQLAlchemy
Base = declarative_base()

# Importar los modelos para que Alembic pueda detectarlos
# (Importar aquí evita problemas de referencias circulares)
from backend.app.models.usuario import Usuario
from backend.app.models.tarea import Tarea

__all__ = ["Base", "Usuario", "Tarea"]
