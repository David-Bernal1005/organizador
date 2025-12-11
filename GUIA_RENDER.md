# Despliegue en Render - Guía Completa

## 📋 Requisitos Previos

1. Cuenta en [Render.com](https://render.com)
2. Repositorio en GitHub con los cambios configurados
3. Base de datos MySQL en Railway (ya tienes esto)

## 🚀 Pasos para Desplegar

### 1. Preparar el Repositorio

Asegúrate de que estos archivos están en Git:
```bash
git add build.sh Procfile render.yaml
git commit -m "Configuración para Render"
git push origin master
```

### 2. Crear el Servicio Web en Render

1. Accede a [https://dashboard.render.com](https://dashboard.render.com)
2. Haz clic en **"New +"** → **"Web Service"**
3. Selecciona tu repositorio `organizador`
4. Completa los campos:

| Campo | Valor |
|-------|-------|
| **Name** | `api-organizador-tareas` |
| **Environment** | `Python 3` |
| **Build Command** | `bash ./build.sh` |
| **Start Command** | `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT` |
| **Plan** | Free (o pagado si necesitas mejor rendimiento) |

### 3. Configurar Variables de Entorno

En Render, ve a **Environment** y añade:

```
DATABASE_URL=mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway
SECRET_KEY=tu_clave_secreta_aleatoria_muy_segura
ALLOWED_ORIGINS=https://tu-frontend.vercel.app,https://tu-dominio.com
```

### 4. Desplegar

Haz clic en **"Create Web Service"** y espera a que se construya la aplicación.

## ✅ Verificar el Despliegue

Una vez desplegado:

```bash
# Ver los logs
curl https://tu-api.onrender.com/

# Debería devolver:
# {"mensaje": "API funcionando"}
```

## 🔗 Conectar el Frontend

Actualiza tu frontend para usar la URL de Render:

```javascript
// En tu servicio de autenticación o configuración
const API_URL = process.env.VITE_API_URL || "https://api-organizador-tareas.onrender.com/api";
```

## 📊 Monitoreo en Render

- **Logs**: En el dashboard, sección "Logs"
- **Métricas**: CPU, memoria, solicitudes
- **Health Check**: Render monitorea `/` automáticamente

## ⚠️ Problemas Comunes

### "Build failed" (Error en construcción)

**Causa**: `create_tables.py` falla en la primera ejecución.

**Solución**: En el dashboard de Render:
1. Ve a **Settings**
2. Desactiva **Auto-Deploy** temporalmente
3. Ejecuta manualmente el despliegue una vez

### "Connection timeout" (Timeout de conexión)

**Causa**: La base de datos no es accesible desde Render.

**Solución**:
- Verifica que la URL de DATABASE_URL es correcta
- En Railway, asegúrate de que es accesible desde cualquier IP
- Usa `pool_pre_ping=True` (ya está configurado)

### "Port 5432 not found"

**Causa**: Estás usando la configuración antigua de PostgreSQL.

**Solución**: La URL debe comenzar con `mysql+pymysql://`

## 🔄 Actualizar la Aplicación

Simplemente haz push a tu repositorio:

```bash
git push origin master
```

Render detectará los cambios automáticamente y redesplegará.

## 💰 Costos

- **Plan Free**: 0.50 USD/hora (máximo 750 horas/mes gratuitas)
- **Plan Pro**: A partir de 7 USD/mes
- Recomendación: Usa Free para desarrollo, Pro para producción

## 🎯 Configuración Recomendada para Producción

```
# En Render → Environment

# Seguridad
SECRET_KEY=<generar con openssl rand -hex 32>

# Base de datos
DATABASE_URL=mysql+pymysql://...

# Frontend permitido (reemplaza con tu URL real)
ALLOWED_ORIGINS=https://tu-frontend.vercel.app

# Otras configuraciones
ENVIRONMENT=production
```

## 📚 Documentación Oficial

- [Render Docs - Web Services](https://render.com/docs/web-services)
- [Render Docs - Environment Variables](https://render.com/docs/environment-variables)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/concepts/)

¡Tu API estará disponible en: `https://api-organizador-tareas.onrender.com`

Reemplaza `api-organizador-tareas` con el nombre que hayas elegido en Render.
