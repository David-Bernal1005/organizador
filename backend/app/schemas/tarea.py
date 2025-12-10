from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255, description="Título de la tarea (obligatorio)")
    descripcion: Optional[str] = Field(None, max_length=1000, description="Descripción de la tarea (opcional)")
    estado: bool = Field(default=False, description="Estado de la tarea (False=pendiente, True=completada)")

class TareaCreate(TareaBase):
    usuario_id: int = Field(..., description="ID del usuario propietario de la tarea")

class TareaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=255)
    descripcion: Optional[str] = Field(None, max_length=1000)
    estado: Optional[bool] = None

class TareaResponse(TareaBase):
    id: int
    usuario_id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True

class TareaListResponse(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str]
    estado: bool
    fecha_creacion: datetime
    usuario_id: int

    class Config:
        from_attributes = True
