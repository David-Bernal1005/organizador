// src/components/TareaItem.jsx
import React, { useState } from 'react';
import { 
  actualizarTarea, 
  marcarCompletada, 
  marcarPendiente, 
  eliminarTarea 
} from '../services/tareaService';
import './TareaItem.css';

export default function TareaItem({ tarea, onActualizada, onEliminada }) {
  const [editando, setEditando] = useState(false);
  const [titulo, setTitulo] = useState(tarea.titulo);
  const [descripcion, setDescripcion] = useState(tarea.descripcion || '');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);

  const handleToggleEstado = async () => {
    setCargando(true);
    setError(null);

    try {
      let tareaActualizada;
      if (tarea.estado) {
        tareaActualizada = await marcarPendiente(tarea.id);
      } else {
        tareaActualizada = await marcarCompletada(tarea.id);
      }
      
      // Actualizar estado local
      if (onActualizada) {
        onActualizada(prev => prev.map(t => t.id === tarea.id ? tareaActualizada : t));
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setCargando(false);
    }
  };

  const handleGuardarEdicion = async () => {
    if (!titulo.trim()) {
      setError('El título es obligatorio');
      return;
    }

    setCargando(true);
    setError(null);

    try {
      const tareaActualizada = await actualizarTarea(tarea.id, {
        titulo,
        descripcion: descripcion || null,
      });

      if (onActualizada) {
        onActualizada(prev => prev.map(t => t.id === tarea.id ? tareaActualizada : t));
      }

      setEditando(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setCargando(false);
    }
  };

  const handleEliminar = async () => {
    if (!window.confirm('¿Estás seguro de que deseas eliminar esta tarea?')) {
      return;
    }

    setCargando(true);
    setError(null);

    try {
      await eliminarTarea(tarea.id);
      if (onEliminada) {
        onEliminada();
      }
    } catch (err) {
      setError(err.message);
      setCargando(false);
    }
  };

  const handleCancelar = () => {
    setTitulo(tarea.titulo);
    setDescripcion(tarea.descripcion || '');
    setEditando(false);
    setError(null);
  };

  const fechaFormato = new Date(tarea.fecha_creacion).toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });

  if (editando) {
    return (
      <div className="tarea-item tarea-edicion">
        <div className="tarea-contenido">
          {error && <div className="alerta alerta-error">{error}</div>}

          <div className="grupo-formulario">
            <input
              type="text"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              placeholder="Título"
              maxLength="255"
              disabled={cargando}
            />
            <small>{titulo.length}/255</small>
          </div>

          <div className="grupo-formulario">
            <textarea
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              placeholder="Descripción"
              maxLength="1000"
              disabled={cargando}
              rows="3"
            />
            <small>{descripcion.length}/1000</small>
          </div>

          <div className="botones-edicion">
            <button
              onClick={handleGuardarEdicion}
              disabled={cargando}
              className="boton boton-exito"
            >
              {cargando ? 'Guardando...' : 'Guardar'}
            </button>
            <button
              onClick={handleCancelar}
              disabled={cargando}
              className="boton boton-secundario"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`tarea-item ${tarea.estado ? 'completada' : 'pendiente'}`}>
      <div className="tarea-contenido">
        <div className="tarea-header">
          <input
            type="checkbox"
            checked={tarea.estado}
            onChange={handleToggleEstado}
            disabled={cargando}
            className="checkbox-estado"
          />
          <div className="tarea-titulo-contenedor">
            <h3 className={tarea.estado ? 'tachado' : ''}>{tarea.titulo}</h3>
            <p className="fecha">{fechaFormato}</p>
          </div>
        </div>

        {tarea.descripcion && (
          <p className="tarea-descripcion">{tarea.descripcion}</p>
        )}

        {error && <div className="alerta alerta-error">{error}</div>}

        <div className="tarea-estado">
          <span className={`badge ${tarea.estado ? 'completada' : 'pendiente'}`}>
            {tarea.estado ? '✓ Completada' : '● Pendiente'}
          </span>
        </div>
      </div>

      <div className="tarea-acciones">
        <button
          onClick={() => setEditando(true)}
          disabled={cargando}
          className="boton boton-secundario"
          title="Editar tarea"
        >
          ✎
        </button>
        <button
          onClick={handleEliminar}
          disabled={cargando}
          className="boton boton-peligro"
          title="Eliminar tarea"
        >
          🗑
        </button>
      </div>
    </div>
  );
}
