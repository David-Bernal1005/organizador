# Gestor de Tareas - CRUD Completo (React + FastAPI)

Sistema completo de gestión de tareas con:
- **Backend**: API REST con FastAPI
- **Frontend**: Interfaz de usuario con React
- **Base de datos**: Integración con SQLAlchemy y Alembic

## Características

### Backend (FastAPI)
✅ Crear tareas con validación de titulo obligatorio  
✅ Listar tareas del usuario o del sistema  
✅ Editar tareas (titulo y descripción)  
✅ Marcar tareas como completada/pendiente  
✅ Eliminar tareas  
✅ Manejo de errores completo  
✅ CORS habilitado para conectar con React  

### Frontend (React)
✅ Interfaz moderna y responsiva  
✅ Crear nuevas tareas  
✅ Listar tareas con filtros (todas, pendientes, completadas)  
✅ Marcar tareas como completadas con checkbox  
✅ Editar tareas en línea  
✅ Eliminar tareas con confirmación  
✅ Estados de carga y errores  
✅ Validaciones en el cliente  

## Estructura del Proyecto

```
organizador/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoint/
│   │   │       ├── auth.py
│   │   │       └── tarea.py (NUEVO)
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   │   ├── tarea.py
│   │   │   └── usuario.py
│   │   └── schemas/
│   │       ├── usuario.py
│   │       └── tarea.py (NUEVO)
│   └── main.py (ACTUALIZADO)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CrearTarea.jsx
│   │   │   ├── CrearTarea.css
│   │   │   ├── ListaTareas.jsx
│   │   │   ├── ListaTareas.css
│   │   │   ├── TareaItem.jsx
│   │   │   └── TareaItem.css
│   │   ├── services/
│   │   │   └── tareaService.js
│   │   ├── App.jsx (NUEVO)
│   │   ├── App.css (NUEVO)
│   │   ├── main.jsx (NUEVO)
│   │   └── pages/
│   ├── index.html (NUEVO)
│   ├── package.json (NUEVO)
│   ├── vite.config.js (NUEVO)
│   └── .gitignore
│
└── requirements.txt
```

## Instalación y Configuración

### 1. Backend (FastAPI)

Las dependencias ya están en `requirements.txt`. Si necesitas instalarlas:

```bash
cd c:\Users\USUARIO\organizador
pip install -r requirements.txt
```

Para agregar `fastapi-cors` si no lo tienes:
```bash
pip install fastapi-cors
```

### 2. Base de Datos

Asegúrate de tener la base de datos creada con las tablas. Si necesitas ejecutar migraciones:

```bash
alembic upgrade head
```

### 3. Frontend (React)

```bash
cd c:\Users\USUARIO\organizador\frontend

# Instalar dependencias
npm install

# O si usas yarn
yarn install
```

## Ejecución

### Ejecutar Backend

```bash
cd c:\Users\USUARIO\organizador
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`  
Documentación interactiva: `http://localhost:8000/docs`

### Ejecutar Frontend

```bash
cd c:\Users\USUARIO\organizador\frontend
npm run dev
```

La aplicación estará disponible en: `http://localhost:5173`

## Endpoints de la API

### Crear Tarea
```
POST /api/tareas/
Content-Type: application/json

{
  "titulo": "Mi tarea",
  "descripcion": "Descripción opcional",
  "estado": false,
  "usuario_id": 1
}
```

### Listar Tareas de Usuario
```
GET /api/tareas/usuario/{usuario_id}
```

### Listar Todas las Tareas
```
GET /api/tareas/
```

### Obtener Tarea Específica
```
GET /api/tareas/{tarea_id}
```

### Actualizar Tarea
```
PUT /api/tareas/{tarea_id}
Content-Type: application/json

{
  "titulo": "Nuevo título",
  "descripcion": "Nueva descripción"
}
```

### Marcar como Completada
```
PATCH /api/tareas/{tarea_id}/completar
```

### Marcar como Pendiente
```
PATCH /api/tareas/{tarea_id}/pendiente
```

### Eliminar Tarea
```
DELETE /api/tareas/{tarea_id}
```

## Uso de la Aplicación

1. **Crear Tarea**
   - Ingresa el título (obligatorio)
   - Agrega descripción (opcional)
   - Haz clic en "Crear Tarea"

2. **Ver Tareas**
   - Las tareas se muestran en la lista
   - Usa los filtros para ver todas, pendientes o completadas

3. **Marcar como Completada**
   - Haz clic en el checkbox de la tarea
   - Se marca automáticamente como completada/pendiente

4. **Editar Tarea**
   - Haz clic en el botón ✎ (editar)
   - Modifica el título o descripción
   - Haz clic en "Guardar"

5. **Eliminar Tarea**
   - Haz clic en el botón 🗑️ (eliminar)
   - Confirma la eliminación

## Validaciones

### Backend
- ✅ Título obligatorio (máx 255 caracteres)
- ✅ Descripción opcional (máx 1000 caracteres)
- ✅ Usuario debe existir
- ✅ Tarea debe existir para actualizar/eliminar
- ✅ Estados HTTP apropiados

### Frontend
- ✅ Validación de título vacío
- ✅ Límite de caracteres
- ✅ Confirmación antes de eliminar
- ✅ Estados de carga
- ✅ Manejo de errores

## Variables de Entorno

Asegúrate de tener un `.env` con:

```
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/organizador
SECRET_KEY=tu_clave_secreta
```

## Troubleshooting

### Error: "CORS policy"
- Asegúrate de que `CORSMiddleware` está configurado en `main.py`
- Verifica que el puerto del backend (8000) es correcto en `tareaService.js`

### Error: "Cannot find module"
- En frontend: ejecuta `npm install`
- En backend: ejecuta `pip install -r requirements.txt`

### Error de Base de Datos
- Verifica que MySQL/MariaDB está corriendo
- Verifica la conexión en `.env`
- Ejecuta `alembic upgrade head`

### Puertos ocupados
- Backend: cambia puerto en `uvicorn` command
- Frontend: cambia puerto en `vite.config.js`

## Próximos Pasos (Opcional)

1. **Autenticación**: Integrar con el endpoint de auth existente
2. **Paginación**: Agregar paginación en lista de tareas
3. **Búsqueda**: Agregar filtro de búsqueda por título
4. **Fechas**: Agregar filtro por rango de fechas
5. **Notificaciones**: Sistema de notificaciones en tiempo real
6. **Exportación**: Exportar tareas a PDF/Excel

## Autor

Creado como parte del sistema organizador de tareas.

## Licencia

Uso libre para el proyecto organizador.
