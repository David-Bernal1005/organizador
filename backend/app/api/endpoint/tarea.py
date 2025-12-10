from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from backend.app.db.session import get_db
from backend.app.models.tarea import Tarea
from backend.app.models.usuario import Usuario
from backend.app.schemas.tarea import (
    TareaCreate,
    TareaUpdate,
    TareaResponse,
    TareaListResponse,
)

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"],
)


# CREATE - Crear una nueva tarea
@router.post("/", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva tarea.
    - **titulo** (obligatorio): Título de la tarea
    - **descripcion** (opcional): Descripción de la tarea
    - **estado**: False para pendiente, True para completada
    - **usuario_id**: ID del usuario propietario
    """
    # Validar que el usuario exista
    usuario = db.query(Usuario).filter(Usuario.id == tarea.usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {tarea.usuario_id} no encontrado"
        )

    # Crear la tarea
    db_tarea = Tarea(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        estado=tarea.estado,
        usuario_id=tarea.usuario_id,
    )
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


# READ - Listar todas las tareas de un usuario
@router.get("/usuario/{usuario_id}", response_model=list[TareaListResponse])
def listar_tareas_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Obtiene todas las tareas de un usuario específico.
    - **usuario_id**: ID del usuario
    """
    # Validar que el usuario exista
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {usuario_id} no encontrado"
        )

    tareas = db.query(Tarea).filter(Tarea.usuario_id == usuario_id).all()
    return tareas


# READ - Listar todas las tareas
@router.get("/", response_model=list[TareaListResponse])
def listar_todas_tareas(db: Session = Depends(get_db)):
    """
    Obtiene todas las tareas del sistema.
    """
    tareas = db.query(Tarea).all()
    return tareas


# READ - Obtener una tarea específica
@router.get("/{tarea_id}", response_model=TareaResponse)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una tarea específica por su ID.
    - **tarea_id**: ID de la tarea
    """
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {tarea_id} no encontrada"
        )
    return tarea


# UPDATE - Actualizar una tarea
@router.put("/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(tarea_id: int, tarea_update: TareaUpdate, db: Session = Depends(get_db)):
    """
    Actualiza una tarea existente.
    Solo se actualizan los campos proporcionados.
    """
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {tarea_id} no encontrada"
        )

    # Actualizar solo los campos que se proporcionan
    if tarea_update.titulo is not None:
        db_tarea.titulo = tarea_update.titulo
    if tarea_update.descripcion is not None:
        db_tarea.descripcion = tarea_update.descripcion
    if tarea_update.estado is not None:
        db_tarea.estado = tarea_update.estado

    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


# UPDATE - Marcar tarea como completada
@router.patch("/{tarea_id}/completar", response_model=TareaResponse)
def marcar_completada(tarea_id: int, db: Session = Depends(get_db)):
    """
    Marca una tarea como completada.
    """
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {tarea_id} no encontrada"
        )

    db_tarea.estado = True
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


# UPDATE - Marcar tarea como pendiente
@router.patch("/{tarea_id}/pendiente", response_model=TareaResponse)
def marcar_pendiente(tarea_id: int, db: Session = Depends(get_db)):
    """
    Marca una tarea como pendiente.
    """
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {tarea_id} no encontrada"
        )

    db_tarea.estado = False
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


# DELETE - Eliminar una tarea
@router.delete("/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    """
    Elimina una tarea específica.
    - **tarea_id**: ID de la tarea a eliminar
    """
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {tarea_id} no encontrada"
        )

    db.delete(db_tarea)
    db.commit()
    return None
