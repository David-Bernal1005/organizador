// src/components/ListaTareas.jsx
import React, { useState, useEffect } from 'react';
import { obtenerTareasPorUsuario, obtenerTodasTareas } from '../services/tareaService';
import TareaItem from './TareaItem';
import './ListaTareas.css';

export default function ListaTareas({ usuarioId, tareaCreada, tareaActualizada, tareaEliminada }) {
  const [tareas, setTareas] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);
  const [filtro, setFiltro] = useState('todas'); // 'todas', 'pendientes', 'completadas'

  // Cargar tareas al montar o cuando cambien las dependencias
  useEffect(() => {
    cargarTareas();
  }, [usuarioId]);

  // Cuando se crea una nueva tarea
  useEffect(() => {
    if (tareaCreada) {
      setTareas([tareaCreada, ...tareas]);
    }
  }, [tareaCreada]);

  // Cuando se actualiza una tarea
  useEffect(() => {
    if (tareaActualizada) {
      setTareas(tareas.map(t => t.id === tareaActualizada.id ? tareaActualizada : t));
    }
  }, [tareaActualizada]);

  // Cuando se elimina una tarea
  useEffect(() => {
    if (tareaEliminada) {
      setTareas(tareas.filter(t => t.id !== tareaEliminada));
    }
  }, [tareaEliminada]);

  const cargarTareas = async () => {
    // Si no hay usuarioId, no cargar nada
    if (!usuarioId) {
      setCargando(false);
      setTareas([]);
      return;
    }

    setCargando(true);
    setError(null);

    try {
      const datos = await obtenerTareasPorUsuario(usuarioId);
      setTareas(datos);
    } catch (err) {
      setError(err.message || 'Error al cargar las tareas');
      console.error('Error al cargar tareas:', err);
    } finally {
      setCargando(false);
    }
  };

  // Filtrar tareas
  const tareasFiltradas = tareas.filter(tarea => {
    if (filtro === 'pendientes') return !tarea.estado;
    if (filtro === 'completadas') return tarea.estado;
    return true;
  });

  if (cargando) {
    return <div className="lista-tareas-container"><p className="cargando">Cargando tareas...</p></div>;
  }

  return (
    <div className="lista-tareas-container">
      <h2>Mis Tareas</h2>

      {!usuarioId && (
        <div className="alerta alerta-advertencia">
          Inicia sesión para ver y gestionar tus tareas
        </div>
      )}

      {error && <div className="alerta alerta-error">{error}</div>}

      {usuarioId && (
        <>
          <div className="controles-filtro">
            <button
              className={`filtro ${filtro === 'todas' ? 'activo' : ''}`}
              onClick={() => setFiltro('todas')}
            >
              Todas ({tareas.length})
            </button>
            <button
              className={`filtro ${filtro === 'pendientes' ? 'activo' : ''}`}
              onClick={() => setFiltro('pendientes')}
            >
              Pendientes ({tareas.filter(t => !t.estado).length})
            </button>
            <button
              className={`filtro ${filtro === 'completadas' ? 'activo' : ''}`}
              onClick={() => setFiltro('completadas')}
            >
              Completadas ({tareas.filter(t => t.estado).length})
            </button>
          </div>

          {tareasFiltradas.length === 0 ? (
            <div className="sin-tareas">
              <p>
                {tareas.length === 0
                  ? 'No hay tareas. ¡Crea una nueva!'
                  : `No hay tareas ${filtro}.`}
              </p>
            </div>
          ) : (
            <div className="tareas-grid">
              {tareasFiltradas.map(tarea => (
                <TareaItem
                  key={tarea.id}
                  tarea={tarea}
                  onActualizada={setTareas}
                  onEliminada={() => setTareas(tareas.filter(t => t.id !== tarea.id))}
                />
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}
