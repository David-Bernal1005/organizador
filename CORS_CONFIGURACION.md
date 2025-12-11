# CORS - Configuración de Múltiples Orígenes

## 📋 Orígenes Configurados Automáticamente

El backend está configurado para permitir automáticamente:

### 1. Desarrollo Local ✅
```
http://localhost:5173          (Vite dev server)
http://localhost:3000          (Alternativo)
http://127.0.0.1:5173         (localhost alternativo)
http://127.0.0.1:3000         (localhost alternativo)
```

### 2. Producción Vercel ✅
```
https://organizador.vercel.app           (Deploy principal)
https://organizador-cyan.vercel.app      (Tu deploy actual)
https://organizador-*.vercel.app         (Todos los preview deployments)
```

---

## 🔧 Configurar Orígenes Personalizados

Si quieres agregar más orígenes (ejemplo: tu propio dominio), edita en **Render Dashboard**:

### Pasos:

1. **Render Dashboard** → `api-organizador-tareas`
2. **Settings** → **Environment Variables**
3. Busca `ALLOWED_ORIGINS`
4. Edita el valor:

### Ejemplo con múltiples orígenes:

```
https://organizador.vercel.app,https://mi-dominio.com,https://app.midominio.com,http://localhost:5173,http://localhost:3000
```

### Formato:
```
origen1,origen2,origen3,...
```

**Separados por comas, sin espacios después de la coma (se limpian automáticamente)**

---

## 📚 Ejemplos Comunes

### Solo Vercel (Producción)
```
ALLOWED_ORIGINS=https://organizador.vercel.app
```

### Vercel + Localhost
```
ALLOWED_ORIGINS=https://organizador.vercel.app,http://localhost:5173
```

### Vercel + Tu Dominio + Localhost
```
ALLOWED_ORIGINS=https://organizador.vercel.app,https://miapp.com,https://www.miapp.com,http://localhost:5173
```

### Todos (Desarrollo + Staging + Producción)
```
ALLOWED_ORIGINS=https://organizador.vercel.app,https://organizador-staging.vercel.app,https://midominio.com,http://localhost:5173,http://localhost:3000
```

---

## ✅ Verificar CORS

Para verificar que está funcionando:

```javascript
// En la consola del navegador
fetch('https://api-organizador-tareas.onrender.com/health')
  .then(r => r.json())
  .then(data => {
    console.log('Status:', data.status);
    console.log('Orígenes permitidos:', data.allowed_origins);
  });
```

Debería devolver algo como:
```javascript
{
  "status": "ok",
  "allowed_origins": [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "https://organizador.vercel.app",
    "https://organizador-cyan.vercel.app"
  ]
}
```

---

## 🔄 Pasos Después de Cambiar ALLOWED_ORIGINS

1. Edita en Render Dashboard
2. Click **Save**
3. En **Deployments**, click **Redeploy** (o espera ~30 segundos)
4. Recarga la página en Vercel (Ctrl+Shift+R o Cmd+Shift+R)
5. Intenta el request nuevamente

---

## 🆘 Si Aún Recibis Error de CORS

### 1. Verifica que la variable está guardada
- Render Dashboard → Settings → Environment
- Busca `ALLOWED_ORIGINS`
- Confirma que está guardada

### 2. Verifica que se hizo Redeploy
- Render Dashboard → Deployments
- Debería haber un nuevo deployment reciente
- Click en él para ver los logs

### 3. Limpia caché del navegador
```javascript
// En consola
localStorage.clear();
sessionStorage.clear();
// Luego recarga (Ctrl+Shift+R)
```

### 4. Verifica la URL del origen
En el error de CORS, aparece:
```
from origin 'https://organizador-cyan.vercel.app'
```

Esa URL debe estar exactamente en `ALLOWED_ORIGINS` (sin espacios).

---

## 📝 Código en backend/main.py

El código automáticamente:

1. Lee `ALLOWED_ORIGINS` de variable de entorno
2. Si no existe, usa orígenes por defecto (localhost)
3. Si está en Render (producción), agrega orígenes de Vercel
4. Limpia espacios en blanco automáticamente
5. Expone endpoint `/health` para verificación

---

## 💡 Tips

- **No uses `*` en CORS** en producción (inseguro)
- **Siempre incluye `https://`** en orígenes de producción
- **Recuerda redeployar** después de cambiar variables
- **Usa el endpoint `/health`** para verificar

---

¿Necesitas que agregue más orígenes? Usa este formato en Render:
```
https://tu-url.com,https://otra-url.com,http://localhost:5173
```
