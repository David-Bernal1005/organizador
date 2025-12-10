// src/components/Register.jsx
import React, { useState } from 'react';
import { register } from '../services/authService';
import './Auth.css';

export default function Register({ onRegisterSuccess }) {
  const [nombre, setNombre] = useState('');
  const [correo, setCorreo] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    if (!nombre.trim() || !correo.trim() || !contraseña) {
      setError('Todos los campos son obligatorios');
      return;
    }
    setCargando(true);
    try {
      const user = await register(nombre.trim(), correo.trim(), contraseña);
      if (onRegisterSuccess) onRegisterSuccess(user);
    } catch (err) {
      setError(err.message || 'Error al registrar');
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="auth-container">
      <h3>Crear cuenta</h3>
      {error && <div className="alerta alerta-error">{error}</div>}
      <form onSubmit={handleSubmit} className="auth-form">
        <label>Nombre</label>
        <input value={nombre} onChange={(e)=>setNombre(e.target.value)} disabled={cargando} />
        <label>Correo</label>
        <input type="email" value={correo} onChange={(e)=>setCorreo(e.target.value)} disabled={cargando} />
        <label>Contraseña</label>
        <input type="password" value={contraseña} onChange={(e)=>setContraseña(e.target.value)} disabled={cargando} />
        <button className="boton boton-primario" type="submit" disabled={cargando}>{cargando ? 'Creando...' : 'Registrarse'}</button>
      </form>
    </div>
  );
}
