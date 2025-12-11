# Despliegue en Vercel - Guía Completa

## 📋 Requisitos Previos

1. Cuenta en [Vercel.com](https://vercel.com)
2. Tu repositorio está en GitHub
3. Backend desplegado en Render (ya hecho)

## 🚀 Pasos para Desplegar en Vercel

### 1. Conectar GitHub a Vercel

1. Accede a [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Haz clic en **"Add New..."** → **"Project"**
3. Selecciona **"Import Git Repository"**
4. Busca `organizador` y selecciona el repositorio
5. Haz clic en **"Import"**

### 2. Configurar el Proyecto

En la página de configuración:

**Project Settings:**
- **Framework Preset**: Vite
- **Build Command**: `npm run build` (ya configurado)
- **Output Directory**: `dist` (ya configurado)
- **Install Command**: `npm install` (ya configurado)

### 3. Configurar Variables de Entorno

En la sección **Environment Variables**, agrega:

```
VITE_API_URL = https://api-organizador-tareas.onrender.com/api
```

Si usas un nombre diferente en Render, reemplaza la URL.

**Importante**: Esta variable debe estar disponible para:
- ✅ Production
- ✅ Preview
- ✅ Development (opcional, pero recomendado)

### 4. Desplegar

Haz clic en **"Deploy"** y espera a que termine.

Una vez completado:
```
✓ Build completado
✓ Deployment exitoso
```

Tu URL será algo como: `https://organizador.vercel.app`

## ✨ Cambios Realizados en el Frontend

### 1. Vite Config Actualizado
```javascript
// vite.config.js
server: {
  proxy: {
    '/api': {
      target: process.env.VITE_API_URL || 'http://localhost:8000',
      changeOrigin: true,
    }
  }
}
```

### 2. Services Actualizados
```javascript
// authService.js
const API_BASE = `${import.meta.env.VITE_API_URL || '/api'}/auth`;

// tareaService.js
const API_BASE_URL = `${import.meta.env.VITE_API_URL || '/api'}/tareas`;
```

Esto permite que:
- ✅ En desarrollo local: usa `http://localhost:8000/api`
- ✅ En Vercel: usa `https://api-organizador-tareas.onrender.com/api`
- ✅ Funciona automáticamente sin cambios de código

### 3. Archivos de Configuración

```
frontend/
├── vercel.json              ← Configuración de Vercel
├── vercel-rewrites.json     ← Rewrites para SPA
├── .env.example             ← Template de variables
├── .env.local               ← Variables locales (ignorado en Git)
├── vite.config.js           ← Actualizado con proxy
└── build.sh                 ← Script de build
```

## 🔗 Conectar Backend y Frontend

### URL del Backend
```
https://api-organizador-tareas.onrender.com
```

### URL del Frontend
```
https://organizador.vercel.app
```

### Actualizar CORS en Backend

Ve a tu dashboard de Render y actualiza:

```
ALLOWED_ORIGINS=https://organizador.vercel.app
```

Si tu frontend tiene otro dominio, actualiza este valor en Render.

## 📊 Monitoreo en Vercel

Después de desplegar:

### Logs
Dashboard → Deployments → Ver logs

### Métricas
Dashboard → Analytics → Ver:
- Request count
- Response time
- Edge Network usage

### Redeploys
Para volver a desplegar sin cambios en el código:
- Dashboard → Deployments → Click en deployment → **Redeploy**

## 🔄 Actualizar la Aplicación

El proceso es automático:

```bash
# Solo necesitas hacer push a GitHub
git add .
git commit -m "Tu mensaje"
git push origin master
```

Vercel detectará los cambios automáticamente y redesplegará.

## ⚠️ Problemas Comunes

### "Module not found"
**Causa**: Falta instalar dependencias
**Solución**: En Vercel, revisa que `npm install` se ejecutó en el build log

### "Cannot find module 'react'"
**Causa**: dependencias no instaladas correctamente
**Solución**: 
1. Elimina `node_modules` localmente
2. Ejecuta `npm install`
3. Haz push nuevamente

### "API returns 404"
**Causa**: `VITE_API_URL` no está configurado correctamente
**Solución**:
1. Ve a Vercel Dashboard
2. Settings → Environment Variables
3. Verifica que `VITE_API_URL` está configurado
4. Click en "Redeploy" en la sección Deployments

### "CORS error"
**Causa**: Backend no tiene el frontend en `ALLOWED_ORIGINS`
**Solución**:
1. Ve a Render Dashboard
2. Environment → Actualiza `ALLOWED_ORIGINS` con tu URL de Vercel
3. Redeploy el backend

## 💡 Verificar la Conexión

Una vez desplegado, abre la consola del navegador (F12):

```javascript
// En la consola, verifica que la URL es correcta
console.log(import.meta.env.VITE_API_URL)
// Debería mostrar: https://api-organizador-tareas.onrender.com/api
```

## 🎯 Estructura Final

```
Frontend (Vercel):  https://organizador.vercel.app
Backend (Render):   https://api-organizador-tareas.onrender.com

Flujo:
1. Usuario accede a https://organizador.vercel.app
2. Frontend (React) carga desde Vercel
3. Frontend hace requests a https://api-organizador-tareas.onrender.com/api
4. Backend procesa y devuelve datos
5. Datos se muestran en el frontend
```

## 📞 Soporte

- [Vercel Docs](https://vercel.com/docs)
- [Vite Docs](https://vitejs.dev/)
- [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 🎉 ¡Listo!

Tu aplicación estará disponible en:
- **Frontend**: https://organizador.vercel.app
- **Backend**: https://api-organizador-tareas.onrender.com

Reemplaza los nombres con los que hayas elegido en Vercel y Render.
