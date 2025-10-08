# Comandos de Ejemplo para la API

Este archivo contiene ejemplos prácticos de cómo usar la API con diferentes herramientas.

## 🌐 Usando curl (Terminal)

### 👥 Operaciones con Usuarios

#### Crear usuario
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario1@ejemplo.com",
    "password": "password123"
  }'
```

#### Obtener todos los usuarios
```bash
curl -X GET "http://localhost:8000/users/"
```

#### Obtener usuario específico
```bash
curl -X GET "http://localhost:8000/users/1"
```

#### Obtener usuarios con paginación
```bash
curl -X GET "http://localhost:8000/users/?skip=0&limit=10"
```

### 📦 Operaciones con Items

#### Crear item para un usuario
```bash
curl -X POST "http://localhost:8000/users/1/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop para desarrollo de software"
  }'
```

#### Obtener todos los items
```bash
curl -X GET "http://localhost:8000/items/"
```

#### Actualizar un item
```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS 15",
    "descripcion": "Laptop renovada para desarrollo"
  }'
```

#### Eliminar un item
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## 🐍 Usando Python requests

### Instalación
```bash
pip install requests
```

### Ejemplos de código

```python
import requests

BASE_URL = "http://localhost:8000"

# Crear usuario
user_data = {
    "email": "python@ejemplo.com",
    "password": "python123"
}
response = requests.post(f"{BASE_URL}/users/", json=user_data)
print(f"Usuario creado: {response.status_code}")
user = response.json()
print(f"ID del usuario: {user['id']}")

# Obtener usuarios
response = requests.get(f"{BASE_URL}/users/")
users = response.json()
print(f"Total usuarios: {len(users)}")

# Crear item
item_data = {
    "nombre": "Teclado Mecánico",
    "descripcion": "Teclado para programar"
}
response = requests.post(f"{BASE_URL}/users/{user['id']}/items/", json=item_data)
print(f"Item creado: {response.status_code}")

# Obtener items
response = requests.get(f"{BASE_URL}/items/")
items = response.json()
print(f"Total items: {len(items)}")
```

## 📱 Usando JavaScript/Fetch

```javascript
const BASE_URL = 'http://localhost:8000';

// Crear usuario
async function createUser() {
    const userData = {
        email: 'js@ejemplo.com',
        password: 'javascript123'
    };
    
    const response = await fetch(`${BASE_URL}/users/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
    });
    
    const user = await response.json();
    console.log('Usuario creado:', user);
    return user;
}

// Obtener usuarios
async function getUsers() {
    const response = await fetch(`${BASE_URL}/users/`);
    const users = await response.json();
    console.log('Usuarios:', users);
    return users;
}

// Crear item
async function createItem(userId) {
    const itemData = {
        nombre: 'Monitor 4K',
        descripcion: 'Monitor para diseño'
    };
    
    const response = await fetch(`${BASE_URL}/users/${userId}/items/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(itemData)
    });
    
    const item = await response.json();
    console.log('Item creado:', item);
    return item;
}

// Uso
createUser().then(user => {
    return createItem(user.id);
}).then(() => {
    return getUsers();
});
```

## 🔄 Flujo Completo de Ejemplo

### Script bash para prueba completa
```bash
#!/bin/bash

API_URL="http://localhost:8000"

echo "🚀 Probando API completa..."

# 1. Crear usuarios
echo "👥 Creando usuarios..."
curl -s -X POST "$API_URL/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@empresa.com", "password": "admin123"}' > /dev/null

curl -s -X POST "$API_URL/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "dev@empresa.com", "password": "dev123"}' > /dev/null

# 2. Listar usuarios
echo "📋 Usuarios creados:"
curl -s -X GET "$API_URL/users/" | jq '.[] | {id, email}'

# 3. Crear items
echo "📦 Creando items..."
curl -s -X POST "$API_URL/users/1/items/" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Servidor", "descripcion": "Servidor de producción"}' > /dev/null

curl -s -X POST "$API_URL/users/2/items/" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "IDE", "descripcion": "Entorno de desarrollo"}' > /dev/null

# 4. Listar items
echo "📋 Items creados:"
curl -s -X GET "$API_URL/items/" | jq '.[] | {id, nombre, propietario_id}'

echo "✅ Prueba completada!"
```

## 🧪 Casos de Prueba

### Casos exitosos
1. **Usuario válido**: email correcto + password ≥ 8 caracteres
2. **Item válido**: nombre requerido + descripción opcional
3. **Actualización**: campos válidos + ID existente

### Casos de error esperados
1. **Email duplicado**: Intentar crear usuario con email existente
2. **Password corto**: Password con menos de 8 caracteres
3. **Usuario inexistente**: Crear item para usuario que no existe
4. **Item inexistente**: Actualizar/eliminar item que no existe

### Ejemplos de errores

#### Email duplicado
```bash
# Primer usuario (éxito)
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@ejemplo.com", "password": "password123"}'

# Segundo usuario con mismo email (error 400)
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@ejemplo.com", "password": "password456"}'
```

#### Password corto
```bash
# Error 422 - Validation Error
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "corto@ejemplo.com", "password": "123"}'
```

#### Usuario inexistente
```bash
# Error 404
curl -X GET "http://localhost:8000/users/999"
```

## 🔍 Respuestas de la API

### Códigos de estado HTTP
- **200**: OK - Operación exitosa
- **201**: Created - Recurso creado
- **400**: Bad Request - Error del cliente
- **404**: Not Found - Recurso no encontrado
- **422**: Unprocessable Entity - Error de validación

### Estructura de respuestas

#### Usuario creado exitosamente
```json
{
  "id": 1,
  "email": "usuario@ejemplo.com",
  "es_activo": true,
  "created_at": "2025-10-07T18:30:00.123456",
  "items": []
}
```

#### Error de validación
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "password"],
      "msg": "La contraseña debe tener al menos 8 caracteres.",
      "input": "123"
    }
  ]
}
```

#### Error personalizado
```json
{
  "detail": "El email ya está registrado"
}
```