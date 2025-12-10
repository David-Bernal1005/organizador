// src/App.jsx
import React, { useState, useEffect } from 'react';
import CrearTarea from './components/CrearTarea';
import ListaTareas from './components/ListaTareas';
import Register from './components/Register';
import Login from './components/Login';
import { getCurrentUser, logout as authLogout } from './services/authService';
import './App.css';

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [tareaCreada, setTareaCreada] = useState(null);
  const [tareaActualizada, setTareaActualizada] = useState(null);
  const [tareaEliminada, setTareaEliminada] = useState(null);

  useEffect(() => {
    const u = getCurrentUser();
    setCurrentUser(u);
  }, []);

  const handleTareaCreada = (tarea) => {
    setTareaCreada(tarea);
    setTimeout(() => setTareaCreada(null), 100);
  };

  const handleLogin = (user) => {
    setCurrentUser(user);
  };

  const handleLogout = () => {
    authLogout();
    setCurrentUser(null);
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>📋 Gestor de Tareas</h1>
        <p>Organiza tus tareas de forma simple y eficiente</p>
      </header>

      <main className="app-main">
        <div className="contenedor">
          <div className="seccion seccion-crear">
            {!currentUser ? (
              <>
                <h2>Bienvenido</h2>
                <p>Accede o crea una cuenta para gestionar tus tareas</p>
                <div style={{display: 'flex', gap: '1rem', marginTop: '1rem'}}>
                  <Login onLoginSuccess={handleLogin} />
                  <Register onRegisterSuccess={handleLogin} />
                </div>
              </>
            ) : (
              <>
                <div style={{display:'flex', justifyContent:'space-between', alignItems:'center'}}>
                  <div>
                    <h2>Hola, {currentUser.nombre}</h2>
                    <p>{currentUser.correo}</p>
                  </div>
                  <div>
                    <button className="boton boton-secundario" onClick={handleLogout}>Cerrar sesión</button>
                  </div>
                </div>
                <CrearTarea 
                  usuarioId={currentUser.id} 
                  onTareaCreada={handleTareaCreada}
                />
              </>
            )}
          </div>

          <div className="seccion seccion-lista">
            <ListaTareas 
              usuarioId={currentUser ? currentUser.id : null}
              tareaCreada={tareaCreada}
              tareaActualizada={tareaActualizada}
              tareaEliminada={tareaEliminada}
            />
          </div>
        </div>
      </main>

      <footer className="app-footer">
        <p>© 2025 Gestor de Tareas - Desarrollado con React</p>
      </footer>
    </div>
  );
}

export default App;
