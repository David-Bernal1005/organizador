// src/services/authService.js
const API_BASE = `${import.meta.env.VITE_API_URL || '/api'}/auth`;
const STORAGE_KEY = 'usuario';

export const register = async (nombre, correo, contraseña) => {
  const res = await fetch(`${API_BASE}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nombre, correo, contraseña }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Error al registrar usuario');
  }
  const user = await res.json();
  setCurrentUser(user);
  return user;
};

export const login = async (correo, contraseña) => {
  const res = await fetch(`${API_BASE}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ correo, contraseña }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Credenciales incorrectas');
  }
  const user = await res.json();
  setCurrentUser(user);
  return user;
};

export const setCurrentUser = (user) => {
  if (user) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(user));
  } else {
    localStorage.removeItem(STORAGE_KEY);
  }
};

export const getCurrentUser = () => {
  try {
    const s = localStorage.getItem(STORAGE_KEY);
    return s ? JSON.parse(s) : null;
  } catch {
    return null;
  }
};

export const logout = () => {
  localStorage.removeItem(STORAGE_KEY);
};
