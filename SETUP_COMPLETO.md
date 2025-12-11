# 🚀 CONFIGURACIÓN COMPLETA - Frontend + Backend

## 📊 Estado de Despliegue

| Componente | Estado | URL |
|-----------|--------|-----|
| **Backend (FastAPI)** | ✅ Configurado | Render |
| **Frontend (React + Vite)** | ✅ Configurado | Vercel |
| **Base de Datos (MySQL)** | ✅ Conectada | Railway |

---

## 🎯 PASO 1: Desplegar Backend en Render

### Prerequisitos
- ✅ Archivos `build.sh`, `Procfile`, `render.yaml` creados
- ✅ `requirements.txt` actualizado con `pymysql`
- ✅ `create_tables.py` mejorado
- ✅ Variables de entorno configuradas en `.env`

### Desplegar en Render (2 minutos)

```
1. Ve a https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Selecciona tu repositorio
4. Completa:
   - Name: api-organizador-tareas
   - Build Command: bash ./build.sh
   - Start Command: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
5. Agrega Environment Variables:
   ├─ DATABASE_URL=mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway
   ├─ SECRET_KEY=tu_clave_secreta
   └─ ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
6. Click "Create Web Service"
```

**URL**: `https://api-organizador-tareas.onrender.com`

---

## 🎯 PASO 2: Desplegar Frontend en Vercel

### Prerequisitos
- ✅ `vercel.json` creado
- ✅ `vite.config.js` actualizado
- ✅ Services actualizados (`authService.js`, `tareaService.js`)
- ✅ Variables de entorno configuradas

### Desplegar en Vercel (2 minutos)

```
1. Ve a https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Selecciona tu repositorio
4. Vercel detecta automáticamente Vite
5. Agrega Environment Variable:
   └─ VITE_API_URL=https://api-organizador-tareas.onrender.com/api
6. Click "Deploy"
```

**URL**: `https://organizador.vercel.app`

---

## 🔗 PASO 3: Conectar Backend y Frontend

### Actualizar CORS en Backend

En Render Dashboard:
1. Ve a tu Web Service
2. Settings → Environment
3. Actualiza `ALLOWED_ORIGINS`:
   ```
   ALLOWED_ORIGINS=https://organizador.vercel.app
   ```
4. Click Save → Redeploy

---

## ✨ Características Implementadas

### Backend (Render + Railway)

```python
✅ FastAPI con CORS configurable
✅ SQLAlchemy ORM
✅ Autenticación JWT
✅ Gestión de tareas
✅ Pool de conexiones con reconnect automático
✅ Variables de entorno seguras
✅ Script de creación de tablas automático
```

### Frontend (Vercel)

```javascript
✅ React 18 + Vite
✅ API URL configurable por entorno
✅ Autenticación con localStorage
✅ Gestión de tareas
✅ CORS proxy en desarrollo
✅ Build optimizado para producción
✅ SPA routing con rewrites
```

### Base de Datos (Railway)

```sql
✅ MySQL en la nube
✅ Tablas: usuarios, tareas
✅ Relaciones: usuario → tareas
✅ Acceso remoto configurado
```

---

## 📁 Estructura del Proyecto Final

```
organizador/
├── 📄 backend/
│   ├── main.py                          (CORS configurable)
│   └── app/
│       ├── api/endpoint/
│       │   ├── auth.py                  (Register, Login)
│       │   └── tarea.py                 (CRUD tareas)
│       ├── models/
│       │   ├── usuario.py               (Tabla usuarios)
│       │   └── tarea.py                 (Tabla tareas)
│       ├── schemas/
│       ├── core/config.py               (DATABASE_URL, SECRET_KEY)
│       └── db/session.py                (SQLAlchemy Engine)
│
├── 📄 frontend/
│   ├── vercel.json                      (Configuración Vercel)
│   ├── vite.config.js                   (Proxy + Build config)
│   ├── .env.example                     (Template variables)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── ListaTareas.jsx
│   │   │   ├── CrearTarea.jsx
│   │   │   └── TareaItem.jsx
│   │   └── services/
│   │       ├── authService.js           (VITE_API_URL)
│   │       └── tareaService.js          (VITE_API_URL)
│
├── 📄 Configuración
│   ├── build.sh                         (Backend build)
│   ├── Procfile                         (Backend start)
│   ├── requirements.txt                 (Python deps)
│   ├── create_tables.py                 (Init DB)
│   ├── .env                             (Secrets - NO SUBIR)
│   ├── .env.example                     (Template)
│   └── .gitignore                       (Git config)
│
└── 📄 Documentación
    ├── CONFIGURACION_RAILWAY.md         (DB setup)
    ├── GUIA_RENDER.md                   (Backend deploy)
    ├── RENDER_CONFIGURADO.md            (Backend summary)
    ├── GUIA_VERCEL.md                   (Frontend deploy)
    └── VERCEL_CONFIGURADO.md            (Frontend summary)
```

---

## 🔐 Variables de Entorno

### Backend (Render)

```
DATABASE_URL=mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway
SECRET_KEY=tu_clave_secreta_mínimo_32_caracteres
ALLOWED_ORIGINS=https://organizador.vercel.app
```

### Frontend (Vercel)

```
VITE_API_URL=https://api-organizador-tareas.onrender.com/api
```

### Local (desarrollo)

```
# Backend (.env)
DATABASE_URL=mysql+pymysql://root:...
SECRET_KEY=...
ALLOWED_ORIGINS=http://localhost:5173

# Frontend (.env.local)
VITE_API_URL=http://localhost:8000/api
```

---

## 🌍 URLs Finales

```
🌐 Frontend:     https://organizador.vercel.app
🔌 Backend API:  https://api-organizador-tareas.onrender.com
📊 Base de Datos: Railway MySQL (privada)
```

### Flujo de Datos

```
Usuario
  ↓
[Vercel] Frontend (React)
  ↓
Request HTTP/HTTPS
  ↓
[Render] Backend (FastAPI)
  ↓
Query/Update
  ↓
[Railway] MySQL Database
```

---

## ✅ Checklist Final

### Backend
- [ ] Render Web Service creado
- [ ] `build.sh` ejecutado sin errores
- [ ] Tablas creadas en Railway
- [ ] Health check: `curl https://api-organizador-tareas.onrender.com/`
- [ ] `ALLOWED_ORIGINS` actualizado con URL de Vercel

### Frontend
- [ ] Vercel Project creado
- [ ] Build completado sin errores
- [ ] `VITE_API_URL` configurado
- [ ] Acceso a la URL de Vercel funciona
- [ ] Login funciona (verifica console.log en F12)

### Integración
- [ ] Frontend llama correctamente al backend
- [ ] Autenticación funciona
- [ ] Tareas se crean y se muestran
- [ ] No hay errores de CORS
- [ ] LocalStorage guarda el usuario

---

## 🔄 Flujo de Desarrollo

### Local

```bash
# Terminal 1 - Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev
```

Accede a: `http://localhost:5173`

### Producción

```bash
# Solo hacer push a GitHub
git add .
git commit -m "Cambios"
git push origin master

# Render y Vercel se actualizan automáticamente
```

---

## 🆘 Troubleshooting

| Problema | Solución |
|----------|----------|
| API returns 404 | Verifica `VITE_API_URL` en Vercel |
| CORS error | Actualiza `ALLOWED_ORIGINS` en Render |
| Build failed en Render | Revisa logs en Render dashboard |
| Build failed en Vercel | Verifica `npm run build` funciona localmente |
| Database connection timeout | Verifica Railway permite conexiones externas |
| "Cannot GET /" en frontend | Vercel rewrites no configurados |

---

## 📚 Documentación de Referencia

| Recurso | URL |
|---------|-----|
| FastAPI | https://fastapi.tiangolo.com |
| SQLAlchemy | https://docs.sqlalchemy.org |
| React | https://react.dev |
| Vite | https://vitejs.dev |
| Render | https://render.com/docs |
| Vercel | https://vercel.com/docs |
| Railway | https://docs.railway.app |

---

## 💡 Tips y Mejoras Futuras

### Seguridad
- [ ] Implementar refresh tokens (no solo localStorage)
- [ ] Agregar HTTPS en todas las conexiones ✅ (Vercel + Render)
- [ ] Validación de email en backend
- [ ] Rate limiting en API

### Performance
- [ ] Lazy loading de componentes
- [ ] Caching en frontend
- [ ] Optimizar imágenes
- [ ] CDN para assets estáticos ✅ (Vercel)

### Features
- [ ] Búsqueda de tareas
- [ ] Filtros por estado
- [ ] Dates de vencimiento
- [ ] Notificaciones
- [ ] Modo oscuro

---

## 🎉 ¡LISTO PARA PRODUCCIÓN!

Tu aplicación está completamente configurada y lista para:

✅ **Desarrollo local** - Todo funciona con `npm run dev` y `uvicorn`
✅ **Staging** - Vercel Preview Deployments
✅ **Producción** - Render + Vercel + Railway

**Acceso Inmediato:**
```
https://organizador.vercel.app
```

**Solo falta:**
1. Hacer los deploys en Render y Vercel
2. Actualizar `ALLOWED_ORIGINS` en Render
3. ¡Disfrutar tu app! 🎊
