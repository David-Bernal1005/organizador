from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.usuario import Usuario
from backend.app.schemas.usuario import UsuarioCrear, UsuarioLogin, UsuarioRespuesta
from backend.app.core.seguridad import encriptar_contraseña, verificar_contraseña

router = APIRouter(prefix="/auth", tags=["Autenticación"])



@router.post("/register", response_model=UsuarioRespuesta)
def registrar_usuario(datos: UsuarioCrear, db: Session = Depends(get_db)):
    print(f"DEBUG: Datos recibidos: {datos}")
    print(f"DEBUG: nombre={datos.nombre}, correo={datos.correo}")

    usuario_existente = db.query(Usuario).filter(Usuario.correo == datos.correo).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    usuario = Usuario(
        nombre=datos.nombre,
        correo=datos.correo,
        contraseña=encriptar_contraseña(datos.contrasena)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


@router.post("/login", response_model=UsuarioRespuesta)
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.correo == datos.correo).first()

    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    if not verificar_contraseña(datos.contrasena, usuario.contraseña):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    return usuario
