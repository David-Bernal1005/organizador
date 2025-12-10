from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    correo = Column(String(255), unique=True, index=True, nullable=False)
    contraseña = Column(String(500), nullable=False)

    # Relación con tareas (1 usuario → muchas tareas)
    tareas = relationship("Tarea", back_populates="usuario", cascade="all, delete-orphan")
