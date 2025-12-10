from pydantic import BaseModel, EmailStr

class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contraseña: str

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        orm_mode = True
