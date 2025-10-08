# Comparación: Proyecto API vs Proyecto Web

Este documento explica las diferencias clave entre el proyecto API original y el proyecto web derivado.

## Arquitectura General

### Proyecto API Original
```
Cliente (Postman/Curl) → FastAPI → SQLAlchemy → SQLite
                     ↓
                   JSON Response
```

### Proyecto Web
```
Navegador → FastAPI → Jinja2 → HTML + CSS
            ↓
         SQLAlchemy → SQLite
```

## Diferencias Técnicas Detalladas

### 1. Respuestas del Servidor

| Aspecto | Proyecto API | Proyecto Web |
|---------|-------------|--------------|
| **Formato de respuesta** | JSON | HTML |
| **Content-Type** | `application/json` | `text/html` |
| **Procesamiento** | Serialización automática | Renderizado de plantillas |
| **Consumo** | Programático | Visual en navegador |

### 2. Manejo de Formularios

#### Proyecto API Original
```python
@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: DatabaseSession):
    # Recibe JSON en el body
    return crud.create_user(db=db, user=user)
```

#### Proyecto Web
```python
@app.post("/users/create")
async def create_user(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    email: str = Form(...),
    password: str = Form(...)
):
    # Recibe datos de formulario HTML
    # Renderiza plantilla en caso de error
    # Redirige en caso de éxito
```

### 3. Navegación y Enlaces

#### Proyecto API
- Sin navegación visual
- URLs documentadas en OpenAPI/Swagger
- Navegación programática entre endpoints

#### Proyecto Web
- Navegación visual con menús
- Enlaces HTML entre páginas
- Breadcrumbs y flujo de usuario intuitivo

### 4. Manejo de Errores

#### Proyecto API
```python
# Retorna HTTP status + JSON
raise HTTPException(status_code=400, detail="El email ya está registrado")
```

#### Proyecto Web
```python
# Renderiza la misma página con mensajes de error
return templates.TemplateResponse(
    "user_form.html",
    {
        "request": request,
        "errors": ["El email ya está registrado"],
        "form_data": {"email": email}
    }
)
```

### 5. Archivos Adicionales

#### Solo en Proyecto API
- `users.py` - Router separado
- Documentación automática Swagger

#### Solo en Proyecto Web
- `templates/` - Plantillas Jinja2
- `static/` - CSS y recursos estáticos
- `start.sh` - Script de inicio
- `populate_db.py` - Datos de ejemplo

### 6. Dependencias

#### Proyecto API
```toml
dependencies = [
    "fastapi[standard]>=0.118.0",
    "sqlalchemy>=2.0.43",
]
```

#### Proyecto Web
```toml
dependencies = [
    "fastapi[standard]>=0.118.0",
    "sqlalchemy>=2.0.43",
    "jinja2>=3.1.2",           # ← Nuevo
    "python-multipart>=0.0.6", # ← Nuevo
]
```

## Ventajas y Desventajas

### Proyecto API

**Ventajas:**
- ✅ Perfecto para integración con otros sistemas
- ✅ Separación clara frontend/backend
- ✅ Escalable para múltiples clientes
- ✅ Ideal para aplicaciones móviles y SPAs
- ✅ Documentación automática con Swagger

**Desventajas:**
- ❌ Requiere cliente separado para interfaz
- ❌ Más complejo para usuarios no técnicos
- ❌ Necesita conocimiento de APIs para usar

### Proyecto Web

**Ventajas:**
- ✅ Interfaz inmediatamente usable
- ✅ No requiere cliente adicional
- ✅ Mejor para aplicaciones CRUD simples
- ✅ SEO friendly (contenido en HTML)
- ✅ Ideal para prototipos rápidos

**Desventajas:**
- ❌ Menos flexible para diferentes tipos de clientes
- ❌ Lógica de presentación mezclada con backend
- ❌ Más difícil de escalar la interfaz

## Casos de Uso Recomendados

### Cuándo usar el Proyecto API
- Aplicaciones móviles
- Single Page Applications (SPAs)
- Microservicios
- Integración con múltiples sistemas
- APIs públicas para terceros

### Cuándo usar el Proyecto Web
- Aplicaciones CRUD empresariales
- Paneles de administración
- Prototipos rápidos
- Aplicaciones internas
- Proyectos educativos

## Evolución Natural

Este proyecto demuestra la evolución típica:

1. **Fase 1**: API REST para operaciones básicas
2. **Fase 2**: Interfaz web para usuarios finales
3. **Fase 3** (futura): Híbrido con API + interfaz web + SPA

## Código Reutilizado

El 80% del código se reutiliza entre ambos proyectos:
- ✅ `database.py` - Idéntico
- ✅ `models.py` - Idéntico  
- ✅ `schemas.py` - Casi idéntico (solo config Pydantic)
- ✅ `crud.py` - Idéntico + una función adicional
- ❌ `main.py` - Completamente diferente
- ❌ `users.py` - Solo en API

Esto demuestra el valor de una arquitectura bien estructurada donde la lógica de negocio es independiente de la capa de presentación.