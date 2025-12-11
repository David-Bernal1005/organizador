// src/services/tareaService.js
const API_BASE_URL = `${import.meta.env.VITE_API_URL || '/api'}/tareas`;

/**
 * Crear una nueva tarea
 */
export const crearTarea = async (titulo, descripcion, usuarioId) => {
  try {
    const response = await fetch(API_BASE_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        titulo,
        descripcion: descripcion || null,
        estado: false,
        usuario_id: usuarioId,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al crear la tarea');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en crearTarea:', error);
    throw error;
  }
};

/**
 * Obtener todas las tareas de un usuario
 */
export const obtenerTareasPorUsuario = async (usuarioId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/usuario/${usuarioId}`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al obtener las tareas');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en obtenerTareasPorUsuario:', error);
    throw error;
  }
};

/**
 * Obtener todas las tareas del sistema
 */
export const obtenerTodasTareas = async () => {
  try {
    const response = await fetch(API_BASE_URL);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al obtener las tareas');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en obtenerTodasTareas:', error);
    throw error;
  }
};

/**
 * Obtener una tarea específica
 */
export const obtenerTarea = async (tareaId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${tareaId}`);

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Tarea no encontrada');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en obtenerTarea:', error);
    throw error;
  }
};

/**
 * Actualizar una tarea
 */
export const actualizarTarea = async (tareaId, actualizaciones) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${tareaId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(actualizaciones),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al actualizar la tarea');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en actualizarTarea:', error);
    throw error;
  }
};

/**
 * Marcar una tarea como completada
 */
export const marcarCompletada = async (tareaId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${tareaId}/completar`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al marcar como completada');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en marcarCompletada:', error);
    throw error;
  }
};

/**
 * Marcar una tarea como pendiente
 */
export const marcarPendiente = async (tareaId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${tareaId}/pendiente`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al marcar como pendiente');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en marcarPendiente:', error);
    throw error;
  }
};

/**
 * Eliminar una tarea
 */
export const eliminarTarea = async (tareaId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${tareaId}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Error al eliminar la tarea');
    }

    return { success: true };
  } catch (error) {
    console.error('Error en eliminarTarea:', error);
    throw error;
  }
};
