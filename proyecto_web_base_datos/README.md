# Proyecto Web Base de Datos

Una aplicación web completa construida con FastAPI, SQLAlchemy y Jinja2 que demuestra operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una interfaz web.

## Descripción

Este proyecto es una evolución del proyecto API original, mostrando cómo transformar una API REST en una aplicación web completa con interfaz de usuario. En lugar de retornar JSON, esta aplicación genera páginas HTML usando plantillas Jinja2.

## Características

- ✅ **Interfaz Web Completa**: Páginas HTML renderizadas del lado del servidor
- ✅ **Operaciones CRUD**: Crear, leer, actualizar y eliminar usuarios e items
- ✅ **Gestión de Usuarios**: Registro y administración de usuarios con validación
- ✅ **Gestión de Items**: Creación y administración de items asociados a usuarios
- ✅ **Diseño Responsivo**: CSS minimalista y profesional sin degradados
- ✅ **Validación de Formularios**: Validación tanto del lado del cliente como del servidor
- ✅ **Manejo de Errores**: Mensajes de error claros y amigables
- ✅ **Base de Datos SQLite**: Almacenamiento persistente de datos

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para Python
- **SQLAlchemy**: ORM para manejo de base de datos
- **Jinja2**: Motor de plantillas para renderizar HTML
- **SQLite**: Base de datos ligera para almacenamiento
- **CSS**: Estilos minimalistas y profesionales
- **Python 3.13+**: Lenguaje de programación

## Estructura del Proyecto

```
proyecto_web_base_datos/
├── main.py              # Aplicación principal con todas las rutas web
├── database.py          # Configuración de la base de datos
├── models.py           # Creación de tablas con SQL raw
├── crud.py             # Operaciones de base de datos
├── schemas.py          # Modelos Pydantic para validación
├── templates/          # Plantillas HTML Jinja2
│   ├── base.html       # Plantilla base
│   ├── index.html      # Página de inicio
│   ├── users.html      # Lista de usuarios
│   ├── user_form.html  # Formulario de usuario
│   ├── user_detail.html # Detalle de usuario
│   ├── items.html      # Lista de items
│   └── item_form.html  # Formulario de item
├── static/             # Archivos estáticos
│   └── style.css       # Estilos CSS
├── pyproject.toml      # Dependencias del proyecto
└── README.md           # Este archivo
```

## Instalación y Configuración

1. **Clonar o navegar al directorio del proyecto:**
   ```bash
   cd proyecto_web_base_datos
   ```

2. **Instalar dependencias usando uv:**
   ```bash
   uv sync
   ```

3. **Activar el entorno virtual:**
   ```bash
   uv shell
   ```

4. **Ejecutar la aplicación:**
   ```bash
   uv run python main.py
   ```
   
   O usando uvicorn directamente:
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Abrir en el navegador:**
   ```
   http://localhost:8000
   ```

## Uso de la Aplicación

### Página Principal
- Accede a `http://localhost:8000` para ver la página de inicio
- Navegación simple entre usuarios e items

### Gestión de Usuarios
- **Ver usuarios**: `/users`
- **Crear usuario**: `/users/create`
- **Ver detalle**: `/users/{id}`
- **Editar usuario**: `/users/{id}/edit`

### Gestión de Items
- **Ver items**: `/items`
- **Crear item**: `/items/create`
- **Crear item para usuario específico**: `/users/{user_id}/items/create`
- **Editar item**: `/items/{id}/edit`
- **Eliminar item**: Botón en la lista de items

## Características del Diseño

### CSS Minimalista y Profesional
- **Variables CSS**: Colores y espaciado consistente
- **Sin degradados**: Diseño limpio y moderno
- **Responsive**: Adaptable a diferentes tamaños de pantalla
- **Componentes reutilizables**: Botones, formularios, tablas, alertas
- **Tipografía clara**: Fuentes del sistema para mejor legibilidad

### Plantillas Jinja2
- **Herencia de plantillas**: Layout base reutilizable
- **Componentes modulares**: Formularios y elementos reutilizables
- **Manejo de estados**: Mensajes de éxito y error
- **Navegación contextual**: Enlaces activos según la página actual

## Diferencias con el Proyecto API Original

| Aspecto | Proyecto API | Proyecto Web |
|---------|-------------|--------------|
| **Respuesta** | JSON | HTML |
| **Cliente** | API clients, Postman | Navegador web |
| **Interfaz** | Sin interfaz | Interfaz web completa |
| **Navegación** | Endpoints programáticos | Enlaces y formularios |
| **Validación** | Solo servidor | Cliente + servidor |
| **Experiencia** | Para desarrolladores | Para usuarios finales |

## Propósito Educativo

Este proyecto demuestra la evolución natural de una API REST hacia una aplicación web completa:

1. **Fase 1 (API)**: Operaciones CRUD básicas con FastAPI
2. **Fase 2 (Web)**: Interfaz de usuario con plantillas Jinja2

Es ideal para enseñar:
- Cómo migrar de API a aplicación web
- Uso de plantillas del lado del servidor
- Manejo de formularios web
- Diseño CSS profesional
- Arquitectura web con FastAPI

## Contribución

Este es un proyecto educativo. Las mejoras y sugerencias son bienvenidas para hacer el código más didáctico y comprensible.

## Licencia

Proyecto educativo de código abierto.