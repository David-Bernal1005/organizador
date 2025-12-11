from pydantic import BaseModel, EmailStr, Field

class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr
    contrasena: str = Field(..., min_length=6, max_length=72, description="Contraseña (6-72 caracteres, límite de bcrypt)")

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str = Field(..., max_length=72)

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        from_attributes = True
