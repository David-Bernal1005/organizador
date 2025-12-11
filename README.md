# 📋 Organizador de Tareas — Fullstack Moderno

Aplicación web de gestión de tareas con autenticación de usuarios. Fullstack moderno con frontend en React y backend en FastAPI.

## 📸 Preview

- **Frontend**: React 18 + Vite + CSS moderno
- **Backend**: FastAPI + SQLAlchemy ORM
- **Base de datos**: MySQL en Railway
- **Hosting**: Vercel (frontend) + Render (backend)
- **Autenticación**: JWT + bcrypt
- **Seguridad**: CORS, validación de email, encriptación de contraseñas

---

## 🛠️ Stack Tecnológico

### Frontend
- **React 18** - Librería UI moderna
- **Vite 5** - Build tool ultrarrápido
- **CSS 3** - Estilos personalizados
- **Fetch API** - Cliente HTTP nativo

### Backend
- **FastAPI** - Framework web asincrónico
- **SQLAlchemy** - ORM para bases de datos
- **PyMySQL** - Driver MySQL
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validación de datos
- **python-jose** - JWT para autenticación
- **passlib + bcrypt** - Encriptación de contraseñas

### DevOps & Deploy
- **Railway** - Hosting base de datos MySQL
- **Render** - Hosting backend FastAPI
- **Vercel** - Hosting frontend React
- **GitHub** - Control de versiones

---

## ✅ Requisitos Previos

### Sistema
- **Python** 3.10 o superior
- **Node.js** v18.x o superior
- **npm** v9.x o superior
- **Git**
- **MySQL** (opcional si usas Railway o similar)

### Verificar instalación
```bash
python --version      # Python 3.10+
node --version        # v18.x.x
npm --version         # v9.x.x
git --version         # v2.x.x
```

---

## 🚀 Ejecución en Local

### 1️⃣ Clonar Repositorio
```bash
git clone https://github.com/David-Bernal1005/organizador.git
cd organizador
```

---

### 2️⃣ Frontend - React + Vite

#### Instalación
```bash
cd frontend
npm install
```

#### Variables de Entorno
```bash
cp .env.example .env
```

Edita `frontend/.env`:
```env
# URL de la API Backend (desarrollo)
VITE_API_URL=http://localhost:8000/api

# Para producción (Vercel):
# VITE_API_URL=https://organizador.onrender.com/api
```

#### Ejecutar en Desarrollo
```bash
npm run dev
```
Frontend estará en: **http://localhost:5173**

#### Build para Producción
```bash
npm run build
npm run preview
```

---

### 3️⃣ Backend - FastAPI + Python

#### Instalación
```bash
cd backend
python -m venv venv
source venv/bin/activate          # macOS/Linux
# o
venv\Scripts\activate              # Windows
```

#### Instalar dependencias
```bash
pip install -r requirements.txt
```

#### Variables de Entorno
```bash
cp .env.example .env
```

Edita `backend/.env`:
```env
# Base de datos MySQL (local)
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/organizador

# Base de datos Railway (producción)
# DATABASE_URL=mysql+pymysql://user:pass@host:port/dbname

# Clave secreta para JWT
SECRET_KEY=tu-clave-secreta-super-segura-aqui

# Puerto
PORT=8000

# Ambiente
ENVIRONMENT=development
```

#### Base de Datos
Necesitas una base de datos MySQL. Opciones:

**Opción 1: MySQL Local**
```bash
# Crear base de datos
mysql -u root -p
> CREATE DATABASE organizador;
> USE organizador;
```

Luego ejecuta:
```bash
python create_tables.py
```

**Opción 2: Railway (Online - Recomendado)**
1. Ve a https://railway.app
2. Crea un proyecto y añade MySQL
3. Copia el `DATABASE_URL` proporcionado
4. Pégalo en `backend/.env`

#### Ejecutar en Desarrollo
```bash
python -m uvicorn backend.main:app --reload
```
Backend estará en: **http://localhost:8000**
Documentación interactiva: **http://localhost:8000/docs**

---

## 🌍 URLs de Producción

### ✨ Frontend - Vercel
📱 **https://organizador-cyan.vercel.app/**

- Despliegue automático en cada push a `master`
- CDN global
- HTTPS automático
- Preview automático en PRs

### 🔌 Backend - Render
🖥️ **https://organizador-tcpn.onrender.com/api**

- Base de datos MySQL en Railway
- Despliegue automático
- Logs en tiempo real
- Health check disponible en `/health`

---

## 📚 Documentación de API

### Base URL
```
http://localhost:8000/api          (Desarrollo)
https://organizador-tcpn.onrender.com/api  (Producción)
```

### Documentación Interactiva
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔐 Autenticación

### 1. POST /auth/register
Registra un nuevo usuario.

**Request:**
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez",
    "correo": "juan@example.com",
    "contrasena": "password123"
  }'
```

**Body esperado:**
```json
{
  "nombre": "Juan Pérez",              // Requerido (string)
  "correo": "juan@example.com",        // Requerido (email válido)
  "contrasena": "password123"          // Requerido (6+ caracteres)
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@example.com"
}
```

**Errores:**
```json
// 400 Bad Request - Correo ya registrado
{
  "detail": "El correo ya está registrado"
}

// 422 Unprocessable Entity - Validación fallida
{
  "detail": [
    {
      "loc": ["body", "contrasena"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

---

### 2. POST /auth/login
Inicia sesión y retorna los datos del usuario.

**Request:**
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "correo": "juan@example.com",
    "contrasena": "password123"
  }'
```

**Body esperado:**
```json
{
  "correo": "juan@example.com",        // Requerido (email)
  "contrasena": "password123"          // Requerido (string)
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@example.com"
}
```

**Errores:**
```json
// 400 Bad Request - Credenciales incorrectas
{
  "detail": "Credenciales incorrectas"
}
```

---

## 📝 Tareas (Tasks)

### 3. POST /tareas
Crea una nueva tarea.

**Request:**
```bash
curl -X POST http://localhost:8000/api/tareas \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Comprar pan",
    "descripcion": "Pan integral sin sal",
    "usuario_id": 1
  }'
```

**Body esperado:**
```json
{
  "titulo": "Comprar pan",             // Requerido (string)
  "descripcion": "Pan integral",       // Opcional (string)
  "usuario_id": 1,                     // Requerido (int)
  "estado": false                      // Opcional (bool, default: false)
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar pan",
  "descripcion": "Pan integral sin sal",
  "estado": false,
  "usuario_id": 1,
  "fecha_creacion": "2025-12-11T10:30:00"
}
```

---

### 4. GET /tareas
Obtiene todas las tareas del sistema.

**Request:**
```bash
curl http://localhost:8000/api/tareas
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "titulo": "Comprar pan",
    "descripcion": "Pan integral sin sal",
    "estado": false,
    "usuario_id": 1,
    "fecha_creacion": "2025-12-11T10:30:00"
  },
  {
    "id": 2,
    "titulo": "Hacer ejercicio",
    "descripcion": "30 minutos de cardio",
    "estado": true,
    "usuario_id": 1,
    "fecha_creacion": "2025-12-10T15:45:00"
  }
]
```

---

### 5. GET /tareas/usuario/{usuario_id}
Obtiene las tareas de un usuario específico.

**Request:**
```bash
curl http://localhost:8000/api/tareas/usuario/1
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "titulo": "Comprar pan",
    "descripcion": "Pan integral sin sal",
    "estado": false,
    "usuario_id": 1,
    "fecha_creacion": "2025-12-11T10:30:00"
  }
]
```

---

### 6. GET /tareas/{tarea_id}
Obtiene una tarea específica.

**Request:**
```bash
curl http://localhost:8000/api/tareas/1
```

**Response (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar pan",
  "descripcion": "Pan integral sin sal",
  "estado": false,
  "usuario_id": 1,
  "fecha_creacion": "2025-12-11T10:30:00"
}
```

---

### 7. PUT /tareas/{tarea_id}
Actualiza una tarea.

**Request:**
```bash
curl -X PUT http://localhost:8000/api/tareas/1 \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Comprar pan integral",
    "descripcion": "Pan integral sin sal tostado",
    "estado": true
  }'
```

**Body esperado:**
```json
{
  "titulo": "Comprar pan integral",    // Opcional
  "descripcion": "Pan integral",       // Opcional
  "estado": true                       // Opcional (bool)
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar pan integral",
  "descripcion": "Pan integral sin sal tostado",
  "estado": true,
  "usuario_id": 1,
  "fecha_creacion": "2025-12-11T10:30:00"
}
```

---

### 8. PATCH /tareas/{tarea_id}/completar
Marca una tarea como completada.

**Request:**
```bash
curl -X PATCH http://localhost:8000/api/tareas/1/completar
```

**Response (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar pan",
  "descripcion": "Pan integral sin sal",
  "estado": true,
  "usuario_id": 1,
  "fecha_creacion": "2025-12-11T10:30:00"
}
```

---

### 9. PATCH /tareas/{tarea_id}/pendiente
Marca una tarea como pendiente.

**Request:**
```bash
curl -X PATCH http://localhost:8000/api/tareas/1/pendiente
```

**Response (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar pan",
  "descripcion": "Pan integral sin sal",
  "estado": false,
  "usuario_id": 1,
  "fecha_creacion": "2025-12-11T10:30:00"
}
```

---

### 10. DELETE /tareas/{tarea_id}
Elimina una tarea.

**Request:**
```bash
curl -X DELETE http://localhost:8000/api/tareas/1
```

**Response (200 OK):**
```json
{
  "success": true
}
```

**Errores:**
```json
// 404 Not Found
{
  "detail": "Tarea no encontrada"
}
```

---

### 11. GET /health
Estado de salud del servidor.

**Request:**
```bash
curl http://localhost:8000/health
```

**Response (200 OK):**
```json
{
  "status": "ok",
  "allowed_origins": [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://organizador-cyan.vercel.app"
  ],
  "allow_origin_regex": "https://.*\\.vercel\\.app$|https://.*\\.onrender\\.com$|..."
}
```

---

## 📊 Códigos de Estado HTTP

| Código | Significado | Ejemplo |
|--------|-------------|---------|
| **200** | OK | GET, PUT, PATCH, DELETE exitosos |
| **201** | Created | POST exitoso (creación) |
| **400** | Bad Request | Datos inválidos o correo duplicado |
| **404** | Not Found | Recurso no existe |
| **422** | Unprocessable Entity | Validación Pydantic fallida |
| **500** | Server Error | Error en el servidor |

---

## 🔧 Variables de Entorno

### Frontend (.env)
```env
# API Backend URL (desarrollo)
VITE_API_URL=http://localhost:8000/api

# Para producción (Vercel):
# VITE_API_URL=https://organizador-tcpn.onrender.com/api
```

### Backend (.env)
```env
# Base de datos MySQL
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/organizador

# Para Railway (producción):
# DATABASE_URL=mysql+pymysql://user:pass@host:port/dbname

# Clave secreta para JWT
SECRET_KEY=tu-clave-secreta-super-segura-aqui

# Puerto
PORT=8000

# Ambiente
ENVIRONMENT=development
```

---

## 📁 Estructura del Proyecto

```
organizador/
├── frontend/                    # React + Vite
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth.css
│   │   │   ├── CrearTarea.jsx
│   │   │   ├── CrearTarea.css
│   │   │   ├── ListaTareas.jsx
│   │   │   ├── ListaTareas.css
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── TareaItem.jsx
│   │   │   └── TareaItem.css
│   │   ├── services/
│   │   │   ├── authService.js  # Registro y login
│   │   │   └── tareaService.js # CRUD de tareas
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.html
│   ├── vite.config.js
│   ├── package.json
│   ├── .env.example
│   └── vercel.json
│
├── backend/                     # FastAPI + Python
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoint/
│   │   │       ├── auth.py      # Rutas autenticación
│   │   │       └── tarea.py     # Rutas CRUD tareas
│   │   ├── core/
│   │   │   ├── config.py        # Configuración
│   │   │   └── seguridad.py     # Funciones criptográficas
│   │   ├── db/
│   │   │   ├── base.py          # Base de datos
│   │   │   └── session.py       # Sesiones SQLAlchemy
│   │   ├── models/
│   │   │   ├── usuario.py       # Modelo Usuario
│   │   │   └── tarea.py         # Modelo Tarea
│   │   ├── schemas/
│   │   │   ├── usuario.py       # Schema Usuario (Pydantic)
│   │   │   └── tarea.py         # Schema Tarea (Pydantic)
│   │   └── __init__.py
│   ├── main.py                  # Punto de entrada FastAPI
│   ├── create_tables.py         # Script crear tablas
│   ├── test_import.py           # Test de importaciones
│   ├── requirements.txt         # Dependencias Python
│   ├── .env.example
│   ├── render.yaml              # Config Render
│   ├── build.sh                 # Script build
│   └── start.sh                 # Script start
│
├── alembic/                     # Migraciones de BD
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── .env                         # Variables locales (NO commitar)
├── .env.example                 # Template variables
├── .gitignore
├── README.md                    # Este archivo
├── README_CRUD_TAREAS.md        # Documentación CRUD
├── Dockerfile
└── alembic.ini
```

---

## 🔒 Seguridad

### Autenticación
- ✅ Contraseñas encriptadas con **bcrypt**
- ✅ Validación de emails con **Pydantic[email]**
- ✅ JWT para futuras sesiones (preparado)

### CORS
- ✅ Permitidos: `localhost:5173`, `localhost:3000`, dominios Vercel y Render
- ✅ Regex dinámico para preview deployments
- ✅ Credenciales permitidas

### Validación de Datos
- ✅ Pydantic schemas para entrada/salida
- ✅ Email válido obligatorio
- ✅ Contraseña mínimo 6 caracteres
- ✅ Campos requeridos

---

## 🚀 Deploy en Vercel (Frontend)

### 1. Conectar repositorio
1. Ve a https://vercel.com
2. New Project → GitHub
3. Selecciona `organizador`
4. Framework preset: **Vite**
5. Deploy

### 2. Configurar variables de entorno
1. Project Settings → Environment Variables
2. Agrega:
   ```
   VITE_API_URL=https://organizador-tcpn.onrender.com/api
   ```
3. Aplica a: **Production** y **Preview**
4. Redeploy

---

## 🚀 Deploy en Render (Backend)

### 1. Conectar repositorio
1. Ve a https://render.com
2. New Web Service → GitHub
3. Selecciona `organizador`
4. Name: `organizador`
5. Runtime: **Python**
6. Build Command: `bash ./build.sh`
7. Start Command: `python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

### 2. Configurar variables de entorno
En Render → Environment:
```
DATABASE_URL=mysql+pymysql://user:pass@host:port/dbname
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_ORIGINS=https://organizador-cyan.vercel.app
```

### 3. Deploy
Render desplegará automáticamente en cada push a `master`.

---

## 🐛 Troubleshooting

### "Cannot POST /api/auth/register" (404)
- ✅ Verifica que `VITE_API_URL` sea correcto en Vercel
- ✅ Redeploy en Vercel después de cambiar variables
- ✅ Revisa DevTools Network → qué URL se llama

### "CORS error en el navegador"
- ✅ Verifica que el backend tiene `allow_origin_regex` configurado
- ✅ Revisa `/health` para ver los orígenes permitidos
- ✅ Redeploy en Render después de cambios CORS

### "Email validation failed" (422)
- ✅ Usa un email válido (ej: `usuario@example.com`)
- ✅ Pydantic rechaza emails sin dominio

### "Password too short" (422)
- ✅ Contraseña mínimo 6 caracteres
- ✅ Máximo 72 caracteres (límite bcrypt)

### "Database connection error"
- ✅ Verifica `DATABASE_URL` en `.env`
- ✅ Asegúrate que la BD está en línea
- ✅ Para Railway, copia la URL exacta

### "Port 8000 already in use"
```bash
# Linux/Mac
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 📞 Contacto & Créditos

**Desarrollador**: David Bernal,Paola Navas  
**Repositorio**: https://github.com/David-Bernal1005/organizador  
**Fecha**: Diciembre 2025

---

## 📄 Licencia

Proyecto educativo para propósitos académicos.

---

## 🎓 Tecnologías Aprendidas

✅ React Hooks (useState, useEffect, useContext)  
✅ API REST con FastAPI  
✅ SQLAlchemy ORM  
✅ Bases de datos relacionales (MySQL)  
✅ Autenticación y encriptación  
✅ Validación con Pydantic  
✅ Diseño responsive  
✅ CORS y seguridad web  
✅ CI/CD con GitHub Actions (preparado)  
✅ Deploy en Vercel y Render  
✅ Control de versiones con Git  

---

**Última actualización**: Diciembre 11, 2025
