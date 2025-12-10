// src/components/CrearTarea.jsx
import React, { useState } from 'react';
import { crearTarea } from '../services/tareaService';
import './CrearTarea.css';

export default function CrearTarea({ usuarioId, onTareaCreada }) {
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);
  const [exito, setExito] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setExito(false);

    if (!usuarioId) {
      setError('Debes iniciar sesión para crear tareas');
      return;
    }

    // Validación: título obligatorio
    if (!titulo.trim()) {
      setError('El título es obligatorio');
      return;
    }

    setCargando(true);

    try {
      const nuevaTarea = await crearTarea(titulo, descripcion, usuarioId);
      setExito(true);
      setTitulo('');
      setDescripcion('');
      
      // Llamar callback para actualizar lista
      if (onTareaCreada) {
        onTareaCreada(nuevaTarea);
      }

      // Limpiar mensaje de éxito después de 3 segundos
      setTimeout(() => setExito(false), 3000);
    } catch (err) {
      setError(err.message || 'Error al crear la tarea');
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="crear-tarea-container">
      <h2>Crear Nueva Tarea</h2>

      {!usuarioId && (
        <div className="alerta alerta-advertencia">Inicia sesión para crear y gestionar tus tareas</div>
      )}

      {error && <div className="alerta alerta-error">{error}</div>}
      {exito && <div className="alerta alerta-exito">¡Tarea creada exitosamente!</div>}

      <form onSubmit={handleSubmit} className="formulario-tarea">
        <div className="grupo-formulario">
          <label htmlFor="titulo">
            Título <span className="requerido">*</span>
          </label>
          <input
            id="titulo"
            type="text"
            value={titulo}
            onChange={(e) => setTitulo(e.target.value)}
            placeholder="Ingresa el título de la tarea"
            disabled={cargando || !usuarioId}
            maxLength="255"
          />
          <small>{titulo.length}/255 caracteres</small>
        </div>

        <div className="grupo-formulario">
          <label htmlFor="descripcion">Descripción (opcional)</label>
          <textarea
            id="descripcion"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            placeholder="Ingresa una descripción (opcional)"
            disabled={cargando}
            rows="4"
            maxLength="1000"
          />
          <small>{descripcion.length}/1000 caracteres</small>
        </div>

        <button 
          type="submit" 
          disabled={cargando || !usuarioId}
          className="boton boton-primario"
        >
          {cargando ? 'Creando...' : 'Crear Tarea'}
        </button>
      </form>
    </div>
  );
}
