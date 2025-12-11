# Frontend Configurado para Vercel ✅

## 📁 Archivos Creados/Actualizados

| Archivo | Propósito |
|---------|-----------|
| `vercel.json` | Configuración de Vercel |
| `.env.example` | Template de variables |
| `.env.local` | Variables de desarrollo (ignorado en Git) |
| `vite.config.js` | Actualizado con proxy a API |
| `build.sh` | Script de compilación |
| `GUIA_VERCEL.md` | Instrucciones detalladas |
| `src/services/authService.js` | Usa `VITE_API_URL` |
| `src/services/tareaService.js` | Usa `VITE_API_URL` |

## 🚀 Desplegar en Vercel (3 minutos)

### Opción 1: Automática (Recomendado)

1. Ve a [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Click en **"Add New"** → **"Project"**
3. Selecciona tu repositorio `organizador`
4. **Presiona Importar**

Vercel detectará automáticamente que es un proyecto Vite y lo configurará.

### Opción 2: Manual

```bash
# Instalar Vercel CLI
npm install -g vercel

# Desplegar
cd frontend
vercel
```

## 🔧 Variables de Entorno (Importante)

En Vercel, agrega en **Settings → Environment Variables**:

```
VITE_API_URL=https://api-organizador-tareas.onrender.com/api
```

Este valor debe estar en:
- ✅ Production
- ✅ Preview  
- ✅ Development (opcional)

## 📋 Checklist Pre-Despliegue

- [ ] Backend desplegado en Render y funcionando
- [ ] Archivo `vercel.json` creado
- [ ] `vite.config.js` actualizado
- [ ] `authService.js` actualizado
- [ ] `tareaService.js` actualizado
- [ ] `.env.example` creado
- [ ] Todos los cambios en Git

Ejecuta:
```bash
cd c:\Users\USUARIO\organizador
git status
# Debería estar limpio
```

## 🔗 URLs Finales

Después del despliegue:

```
🌐 Frontend:   https://organizador.vercel.app
🔌 Backend:    https://api-organizador-tareas.onrender.com/api
```

### Actualizar Backend

Para que el backend acepte requests del frontend, actualiza en Render:

**Dashboard → Settings → Environment**

Cambia:
```
ALLOWED_ORIGINS=https://organizador.vercel.app
```

## ✨ Cómo Funciona

```
Usuario abre: https://organizador.vercel.app
    ↓
Frontend (React) se carga desde Vercel
    ↓
Usuario hace login
    ↓
Frontend envía request a: https://api-organizador-tareas.onrender.com/api/auth/login
    ↓
Backend procesa y responde
    ↓
Frontend muestra datos al usuario
```

## 🔄 Actualizar la App

Simplemente haz push a GitHub:

```bash
git add .
git commit -m "Tu cambio"
git push origin master
```

Vercel detectará automáticamente y redesplegará.

## 📊 Monitorear Despliegue

En Vercel Dashboard:
- **Logs**: Ver qué sucede durante build
- **Deployments**: Ver historial de despliegues
- **Analytics**: Tráfico y rendimiento
- **Settings**: Cambiar variables sin redeployar

## 🆘 Troubleshooting

### "API_URL is undefined"
```javascript
// Verificar en consola del navegador
console.log(import.meta.env.VITE_API_URL)
```
Si muestra `undefined`, la variable no está configurada en Vercel.

### "CORS error en requests"
1. Verifica que `ALLOWED_ORIGINS` en Render incluye tu URL de Vercel
2. Redeploy el backend en Render

### "Build failed"
Revisa los logs en Vercel → Deployments → Click en deployment fallido

## 📚 Documentación

- [Vercel Docs](https://vercel.com/docs)
- [Vite Docs](https://vitejs.dev/)
- [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 💡 Tips de Seguridad

- ✅ `VITE_API_URL` es seguro exponer en el frontend (es una variable pública)
- ✅ Nunca expongas `SECRET_KEY` del backend en variables del frontend
- ✅ Las credentials se guardan en localStorage (considera agregar tokens JWT en el futuro)

---

## 🎯 Resumen de Cambios

Tu aplicación está lista para Vercel. Los cambios permitieron:

1. **Variable de entorno dinámica**: `VITE_API_URL` se configura en Vercel
2. **Desarrollo local**: Usa proxy local (`http://localhost:8000`)
3. **Producción**: Usa API remota en Render
4. **SPA Compatible**: Vercel redirige todas las rutas a `index.html`

**¡Todo está listo! Solo sigue los 3 pasos de despliegue.** 🚀
