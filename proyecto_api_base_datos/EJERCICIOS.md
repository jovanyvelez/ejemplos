# Ejercicios Prácticos para el Proyecto API

Este archivo contiene ejercicios progresivos para practicar y extender el proyecto API.

## 🎯 Nivel Básico

### Ejercicio 1: Validación de Email Único
**Objetivo**: Asegurar que no se puedan crear usuarios con emails duplicados.

**Tareas**:
1. Modifica `users.py` para verificar emails duplicados antes de crear
2. Retorna un error 400 con mensaje descriptivo
3. Prueba con el script `test_api.sh`

**Pistas**:
```python
# En users.py
db_user = crud.get_user_by_email(db, email=user.email)
if db_user:
    raise HTTPException(status_code=400, detail="Email ya registrado")
```

### Ejercicio 2: Endpoint de Desactivación
**Objetivo**: Crear endpoint para desactivar usuarios en lugar de eliminarlos.

**Tareas**:
1. Crear función `deactivate_user` en `crud.py`
2. Añadir endpoint `PUT /users/{user_id}/deactivate` en `users.py`
3. Actualizar campo `es_activo` a `False`

**Estructura esperada**:
```python
@router.put("/users/{user_id}/deactivate")
async def deactivate_user(user_id: int, db: DatabaseSession):
    # Tu código aquí
    pass
```

### Ejercicio 3: Paginación Mejorada
**Objetivo**: Añadir metadata de paginación a la respuesta.

**Tareas**:
1. Crear esquema `PaginatedUsers` en `schemas.py`
2. Modificar endpoint `/users/` para retornar metadata
3. Incluir: total, página, límite, siguiente página

**Estructura esperada**:
```python
class PaginatedUsers(BaseModel):
    items: list[User]
    total: int
    page: int
    limit: int
    has_next: bool
```

## 🎯 Nivel Intermedio

### Ejercicio 4: Filtro de Usuarios Activos
**Objetivo**: Permitir filtrar usuarios por estado activo/inactivo.

**Tareas**:
1. Añadir parámetro `activo: bool = None` al endpoint `/users/`
2. Modificar `crud.get_users()` para filtrar por estado
3. Documentar el parámetro en la función

**Ejemplo de uso**:
```bash
GET /users/?activo=true   # Solo usuarios activos
GET /users/?activo=false  # Solo usuarios inactivos
GET /users/              # Todos los usuarios
```

### Ejercicio 5: Búsqueda de Usuarios
**Objetivo**: Implementar búsqueda de usuarios por email.

**Tareas**:
1. Añadir parámetro `buscar: str = None` al endpoint `/users/`
2. Crear función `search_users_by_email` en `crud.py`
3. Usar `LIKE` en SQL para búsqueda parcial

**SQL esperado**:
```sql
SELECT * FROM users WHERE email LIKE '%search_term%'
```

### Ejercicio 6: Items por Usuario
**Objetivo**: Crear endpoint específico para items de un usuario.

**Tareas**:
1. Añadir endpoint `GET /users/{user_id}/items/`
2. Crear función `get_user_items` en `crud.py`
3. Retornar lista de items del usuario específico

### Ejercicio 7: Timestamps Automáticos
**Objetivo**: Añadir campo `updated_at` que se actualice automáticamente.

**Tareas**:
1. Modificar `models.py` para añadir `updated_at` a ambas tablas
2. Actualizar funciones de actualización en `crud.py`
3. Modificar esquemas en `schemas.py`

## 🎯 Nivel Avanzado

### Ejercicio 8: Validación Avanzada de Items
**Objetivo**: Añadir validaciones complejas para items.

**Tareas**:
1. El nombre del item debe ser único por usuario
2. La descripción no puede tener más de 500 caracteres
3. Crear validador personalizado en `schemas.py`

**Validador esperado**:
```python
@field_validator('descripcion')
def validate_descripcion(cls, value):
    if value and len(value) > 500:
        raise ValueError('Descripción muy larga')
    return value
```

### Ejercicio 9: Soft Delete para Items
**Objetivo**: Implementar borrado lógico en lugar de físico.

**Tareas**:
1. Añadir campo `deleted_at` a tabla items
2. Modificar `delete_item` para marcar como eliminado
3. Filtrar items eliminados en consultas normales
4. Crear endpoint para "restaurar" items

### Ejercicio 10: Estadísticas de la API
**Objetivo**: Crear endpoint con estadísticas generales.

**Tareas**:
1. Crear endpoint `GET /stats/`
2. Retornar: total usuarios, usuarios activos, total items, items por usuario
3. Crear esquema `APIStats` para la respuesta

**Respuesta esperada**:
```json
{
  "total_users": 10,
  "active_users": 8,
  "total_items": 25,
  "average_items_per_user": 2.5,
  "most_active_user": {
    "email": "user@example.com",
    "items_count": 5
  }
}
```

## 🎯 Nivel Experto

### Ejercicio 11: Rate Limiting
**Objetivo**: Implementar límite de peticiones por IP.

**Tareas**:
1. Instalar `slowapi`: `pip install slowapi`
2. Añadir middleware de rate limiting
3. Limitar a 100 peticiones por minuto por IP

### Ejercicio 12: Autenticación JWT
**Objetivo**: Proteger endpoints con autenticación.

**Tareas**:
1. Instalar `python-jose`: `pip install python-jose[cryptography]`
2. Crear endpoint `/login/` que retorne JWT
3. Proteger endpoints de creación/modificación
4. Añadir middleware de autenticación

### Ejercicio 13: Testing Automatizado
**Objetivo**: Crear suite de tests para la API.

**Tareas**:
1. Instalar `pytest`: `pip install pytest httpx`
2. Crear `test_main.py` con tests para todos los endpoints
3. Usar `TestClient` de FastAPI
4. Incluir tests para casos de error

**Ejemplo de test**:
```python
def test_create_user():
    response = client.post("/users/", json={
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
```

### Ejercicio 14: Documentación Avanzada
**Objetivo**: Mejorar la documentación automática de FastAPI.

**Tareas**:
1. Añadir descripciones detalladas a todos los endpoints
2. Incluir ejemplos de requests/responses
3. Agrupar endpoints con tags
4. Añadir metadata del API

**Ejemplo**:
```python
@router.post("/users/", 
             response_model=schemas.User,
             summary="Crear nuevo usuario",
             description="Crea un nuevo usuario con email y password",
             response_description="Usuario creado exitosamente",
             tags=["usuarios"])
```

### Ejercicio 15: Migración a PostgreSQL
**Objetivo**: Migrar de SQLite a PostgreSQL.

**Tareas**:
1. Instalar `psycopg2`: `pip install psycopg2-binary`
2. Crear base de datos PostgreSQL
3. Modificar `DATABASE_URL` en `.env`
4. Adaptar SQL si es necesario
5. Crear script de migración de datos

## 🧪 Tests de Validación

Para cada ejercicio, crea tests que verifiquen:

1. **Casos exitosos**: Funcionalidad correcta
2. **Casos de error**: Manejo apropiado de errores  
3. **Casos edge**: Valores límite y casos especiales
4. **Performance**: Tiempo de respuesta aceptable

## 📝 Entregables

Para cada ejercicio, entrega:

1. **Código modificado**: Archivos con los cambios
2. **Documentación**: Comentarios explicando el código
3. **Tests**: Al menos 3 tests por funcionalidad
4. **Ejemplos**: Comandos curl para probar

## 🏆 Proyecto Final

**Mega Ejercicio**: Combina todos los ejercicios anteriores para crear una API completa con:

- ✅ Autenticación JWT
- ✅ Rate limiting
- ✅ Paginación avanzada
- ✅ Búsqueda y filtros
- ✅ Soft delete
- ✅ Estadísticas
- ✅ Tests completos
- ✅ PostgreSQL
- ✅ Documentación profesional

## 🎯 Criterios de Evaluación

| Criterio | Básico | Intermedio | Avanzado |
|----------|--------|------------|----------|
| **Funcionalidad** | Funciona correctamente | + Manejo de errores | + Optimización |
| **Código** | Readable | + Documentado | + Patterns |
| **Tests** | Tests básicos | + Edge cases | + Coverage 100% |
| **Documentación** | README actualizado | + Ejemplos | + API docs |

¡Buena suerte con los ejercicios! 🚀