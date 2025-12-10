// src/components/Login.jsx
import React, { useState } from 'react';
import { login } from '../services/authService';
import './Auth.css';

export default function Login({ onLoginSuccess }) {
  const [correo, setCorreo] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    if (!correo.trim() || !contraseña) {
      setError('Correo y contraseña son obligatorios');
      return;
    }
    setCargando(true);
    try {
      const user = await login(correo.trim(), contraseña);
      if (onLoginSuccess) onLoginSuccess(user);
    } catch (err) {
      setError(err.message || 'Error al iniciar sesión');
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="auth-container">
      <h3>Iniciar sesión</h3>
      {error && <div className="alerta alerta-error">{error}</div>}
      <form onSubmit={handleSubmit} className="auth-form">
        <label>Correo</label>
        <input type="email" value={correo} onChange={(e)=>setCorreo(e.target.value)} disabled={cargando} />
        <label>Contraseña</label>
        <input type="password" value={contraseña} onChange={(e)=>setContraseña(e.target.value)} disabled={cargando} />
        <button className="boton boton-primario" type="submit" disabled={cargando}>{cargando ? 'Entrando...' : 'Entrar'}</button>
      </form>
    </div>
  );
}
