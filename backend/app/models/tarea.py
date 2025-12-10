from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)  # obligatorio
    descripcion = Column(Text, nullable=True)
    estado = Column(Boolean, default=False)  # False = pendiente, True = completada
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    # Relación con usuario
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)

    usuario = relationship("Usuario", back_populates="tareas")
