# Proyecto API Base de Datos

Una API REST completa construida con FastAPI y SQLAlchemy que demuestra operaciones CRUD (Crear, Leer, Actualizar, Eliminar) fundamentales para el desarrollo backend.

## 🎯 Objetivo Educativo

Este proyecto está diseñado para enseñar los **conceptos fundamentales del desarrollo de APIs REST** usando tecnologías modernas de Python. Es el primer paso en la serie de proyectos que culmina con una aplicación web completa.

### 📚 ¿Qué aprenderás?

- **FastAPI**: Framework moderno para crear APIs rápidas
- **SQLAlchemy**: ORM para manejo de bases de datos
- **Pydantic**: Validación de datos y serialización
- **SQL Raw**: Consultas directas a la base de datos
- **Arquitectura REST**: Principios y mejores prácticas
- **Manejo de errores**: Respuestas HTTP apropiadas
- **Validación de datos**: Entrada y salida de datos segura

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito | Ventajas |
|------------|-----------|----------|
| **FastAPI** | Framework web | Rápido, automático docs, type hints |
| **SQLAlchemy** | ORM/Database | Abstracción de BD, migraciones |
| **Pydantic** | Validación | Type safety, documentación automática |
| **SQLite** | Base de datos | Ligera, sin configuración |
| **Python 3.13+** | Lenguaje | Moderno, tipado, async/await |

## 📁 Estructura del Proyecto

```
proyecto_api_base_datos/
├── main.py              # 🚀 Punto de entrada de la aplicación
├── users.py            # 👥 Rutas y lógica de usuarios
├── database.py         # 🗄️ Configuración de base de datos
├── models.py           # 📋 Definición de tablas (SQL raw)
├── crud.py             # 🔄 Operaciones CRUD
├── schemas.py          # ✅ Modelos Pydantic para validación
├── pyproject.toml      # 📦 Dependencias del proyecto
├── sql_app_ejemplo.db  # 💾 Base de datos SQLite (generada)
└── README.md           # 📖 Este archivo
```

### 🔍 Explicación de cada archivo:

#### `main.py` - Aplicación Principal
```python
# Punto de entrada que configura FastAPI y registra las rutas
from fastapi import FastAPI
from models import crear_tablas
from users import router as users

app = FastAPI(title="Ejemplo API con FastAPI y SQLAlchemy")
app.include_router(users)
```

#### `users.py` - Rutas de la API
- **Endpoints REST** para operaciones CRUD
- **Manejo de dependencias** con inyección
- **Validación automática** con Pydantic
- **Respuestas estructuradas** en JSON

#### `database.py` - Configuración de BD
- **Conexión a la base de datos** con SQLAlchemy
- **Patrón de dependencia** para sesiones
- **Configuración de motor** y pool de conexiones

#### `models.py` - Esquema de Base de Datos
- **Creación de tablas** con SQL raw
- **Relaciones entre tablas** (FK)
- **Campos con valores por defecto**

#### `crud.py` - Operaciones de Datos
- **Funciones CRUD** separadas por responsabilidad
- **Consultas SQL raw** con parámetros seguros
- **Manejo de errores** de base de datos

#### `schemas.py` - Validación de Datos
- **Modelos Pydantic** para entrada y salida
- **Validación automática** de tipos
- **Documentación automática** de la API

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.13 o superior
- pip o uv (gestor de paquetes)

### Pasos de instalación:

1. **Navegar al directorio del proyecto:**
   ```bash
   cd proyecto_api_base_datos
   ```

2. **Instalar dependencias:**
   ```bash
   # Con pip
   pip install "fastapi[standard]>=0.118.0" "sqlalchemy>=2.0.43"
   
   # Con uv (recomendado)
   uv sync
   ```

3. **Ejecutar la aplicación:**
   ```bash
   # Método 1: Directamente
   python main.py
   
   # Método 2: Con uvicorn
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Verificar que funciona:**
   - API disponible en: `http://localhost:8000`
   - Documentación automática en: `http://localhost:8000/docs`
   - Esquema OpenAPI en: `http://localhost:8000/redoc`

## 📡 Endpoints de la API

### 👥 Gestión de Usuarios

| Método | Endpoint | Descripción | Cuerpo de la petición |
|--------|----------|-------------|----------------------|
| `POST` | `/users/` | Crear nuevo usuario | `{"email": "user@example.com", "password": "password123"}` |
| `GET` | `/users/` | Listar usuarios | - |
| `GET` | `/users/{user_id}` | Obtener usuario por ID | - |

### 📦 Gestión de Items

| Método | Endpoint | Descripción | Cuerpo de la petición |
|--------|----------|-------------|----------------------|
| `POST` | `/users/{user_id}/items/` | Crear item para usuario | `{"nombre": "Mi item", "descripcion": "Descripción"}` |
| `GET` | `/items/` | Listar todos los items | - |
| `PUT` | `/items/{item_id}` | Actualizar item | `{"nombre": "Nuevo nombre", "descripcion": "Nueva desc"}` |
| `DELETE` | `/items/{item_id}` | Eliminar item | - |

## 🧪 Ejemplos de Uso

### 1. Crear un usuario
```bash
curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"email": "juan@ejemplo.com", "password": "password123"}'
```

**Respuesta:**
```json
{
  "id": 1,
  "email": "juan@ejemplo.com",
  "es_activo": true,
  "created_at": "2025-10-07T18:30:00",
  "items": []
}
```

### 2. Obtener todos los usuarios
```bash
curl -X GET "http://localhost:8000/users/"
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "email": "juan@ejemplo.com",
    "es_activo": true,
    "created_at": "2025-10-07T18:30:00",
    "items": []
  }
]
```

### 3. Crear un item para un usuario
```bash
curl -X POST "http://localhost:8000/users/1/items/" \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Laptop", "descripcion": "Laptop para trabajo"}'
```

### 4. Obtener todos los items
```bash
curl -X GET "http://localhost:8000/items/"
```

### 5. Actualizar un item
```bash
curl -X PUT "http://localhost:8000/items/1" \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Laptop Dell", "descripcion": "Laptop Dell para trabajo"}'
```

### 6. Eliminar un item
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## 📊 Esquema de Base de Datos

### Tabla `users`
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email VARCHAR NOT NULL,
    hashed_password VARCHAR NOT NULL,
    es_activo BOOLEAN NOT NULL,
    created_at DATETIME DEFAULT (datetime('now'))
);
```

### Tabla `items`
```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    descripcion VARCHAR,
    created_at DATETIME DEFAULT (datetime('now')),
    propietario_id INTEGER,
    FOREIGN KEY(propietario_id) REFERENCES users(id)
);
```

### Relaciones
- Un **usuario** puede tener **muchos items** (relación 1:N)
- Cada **item** pertenece a **un solo usuario**

## 🔧 Configuración Avanzada

### Variables de Entorno
Crea un archivo `.env` para configurar la base de datos:

```env
DATABASE_URL=sqlite:///./sql_app_ejemplo.db
```

### Otras bases de datos soportadas:
```env
# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost/dbname

# MySQL
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

## 🎓 Conceptos Clave Explicados

### 1. **REST API Principles**
- **Recursos**: `/users`, `/items` representan entidades
- **Métodos HTTP**: GET (leer), POST (crear), PUT (actualizar), DELETE (eliminar)
- **Estado**: API sin estado (stateless)
- **Respuestas consistentes**: Códigos HTTP apropiados

### 2. **Dependency Injection**
```python
def get_db():
    with SessionLocal() as session:
        yield session

# FastAPI inyecta automáticamente la dependencia
async def create_user(user: UserCreate, db: DatabaseSession):
    # db es inyectada automáticamente
```

### 3. **Validación con Pydantic**
```python
class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def password_length(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters')
        return value
```

### 4. **SQL Raw vs ORM**
Este proyecto usa **SQL raw** para propósitos educativos:
```python
# SQL Raw (usado en este proyecto)
result = db.execute(text("SELECT * FROM users WHERE id = :user_id"), {"user_id": user_id})

# ORM (alternativa)
result = db.query(User).filter(User.id == user_id).first()
```

### 5. **Manejo de Errores**
```python
if not user:
    raise HTTPException(status_code=404, detail="User not found")
```

## 🔍 Herramientas de Desarrollo

### 1. **Documentación Automática**
- FastAPI genera documentación automática
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 2. **Testing con curl**
Todos los endpoints se pueden probar con curl (ver ejemplos arriba)

### 3. **Postman/Insomnia**
Importa la documentación OpenAPI desde `http://localhost:8000/openapi.json`

### 4. **Logs de SQLAlchemy**
```python
engine = create_engine(DATABASE_URL, echo=True)  # echo=True muestra SQL
```

## 🚧 Próximos Pasos

Este proyecto API es la **base** para el siguiente proyecto educativo:

### **proyecto_web_base_datos** 
- ✅ Misma lógica backend
- ✅ Interfaz web con Jinja2
- ✅ Formularios HTML
- ✅ CSS profesional
- ✅ Experiencia de usuario completa

## 🎯 Ejercicios Propuestos

### Básico:
1. **Agregar validación** de email único en `users.py`
2. **Implementar endpoint** para desactivar usuarios
3. **Añadir paginación** a la lista de usuarios

### Intermedio:
4. **Crear endpoint** para obtener items de un usuario específico
5. **Implementar búsqueda** de usuarios por email
6. **Agregar campo** `updated_at` a las tablas

### Avanzado:
7. **Implementar autenticación** con JWT
8. **Añadir middleware** para logging de requests
9. **Crear tests unitarios** con pytest

## 🐛 Troubleshooting

### Error: "No module named 'fastapi'"
```bash
pip install "fastapi[standard]"
```

### Error: "Unable to open database file"
```bash
# Verificar permisos del directorio
chmod 755 .
```

### Error: "Address already in use"
```bash
# Cambiar puerto
uvicorn main:app --port 8001
```

## 🤝 Contribución

Este es un proyecto educativo. Las mejoras y sugerencias son bienvenidas:

1. Hacer más claro el código
2. Añadir más ejemplos
3. Mejorar la documentación
4. Corregir errores

## 📄 Licencia

Proyecto educativo de código abierto.

---

## 🎉 ¡Felicitaciones!

Si has llegado hasta aquí, ya dominas los conceptos fundamentales de:
- ✅ APIs REST con FastAPI
- ✅ Operaciones CRUD
- ✅ Validación de datos
- ✅ Manejo de bases de datos
- ✅ Arquitectura backend moderna

**¡Estás listo para el siguiente nivel: proyecto_web_base_datos!** 🚀
