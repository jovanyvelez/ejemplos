#!/bin/bash

# Script para probar la API completamente
# Asegúrate de que la aplicación esté corriendo en localhost:8000

API_URL="http://localhost:8000"
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Probando API completa...${NC}"
echo ""

# Función para verificar si la API está corriendo
check_api() {
    if ! curl -s "$API_URL" > /dev/null; then
        echo -e "${RED}❌ Error: La API no está corriendo en $API_URL${NC}"
        echo "   Ejecuta: python main.py"
        exit 1
    fi
}

# Función para hacer peticiones con manejo de errores
api_request() {
    local method=$1
    local endpoint=$2
    local data=$3
    local description=$4
    
    echo -e "${YELLOW}➤ $description${NC}"
    
    if [ -n "$data" ]; then
        response=$(curl -s -w "\n%{http_code}" -X "$method" "$API_URL$endpoint" \
                   -H "Content-Type: application/json" \
                   -d "$data")
    else
        response=$(curl -s -w "\n%{http_code}" -X "$method" "$API_URL$endpoint")
    fi
    
    http_code=$(tail -n1 <<< "$response")
    body=$(sed '$ d' <<< "$response")
    
    if [[ $http_code -ge 200 && $http_code -lt 300 ]]; then
        echo -e "${GREEN}✅ Éxito ($http_code)${NC}"
        if command -v jq > /dev/null; then
            echo "$body" | jq '.'
        else
            echo "$body"
        fi
    else
        echo -e "${RED}❌ Error ($http_code)${NC}"
        echo "$body"
    fi
    echo ""
}

# Verificar que la API esté corriendo
check_api

# 1. Crear usuarios
echo -e "${BLUE}👥 === OPERACIONES CON USUARIOS ===${NC}"
api_request "POST" "/users/" \
    '{"email": "admin@empresa.com", "password": "admin123"}' \
    "Crear usuario administrador"

api_request "POST" "/users/" \
    '{"email": "dev@empresa.com", "password": "developer123"}' \
    "Crear usuario desarrollador"

api_request "POST" "/users/" \
    '{"email": "test@empresa.com", "password": "testing123"}' \
    "Crear usuario de pruebas"

# 2. Probar error de email duplicado
api_request "POST" "/users/" \
    '{"email": "admin@empresa.com", "password": "otrapass123"}' \
    "Intentar crear usuario con email duplicado (debe fallar)"

# 3. Probar error de password corto
api_request "POST" "/users/" \
    '{"email": "corto@empresa.com", "password": "123"}' \
    "Intentar crear usuario con password corto (debe fallar)"

# 4. Listar usuarios
api_request "GET" "/users/" "" \
    "Obtener lista de todos los usuarios"

# 5. Obtener usuario específico
api_request "GET" "/users/1" "" \
    "Obtener usuario con ID 1"

# 6. Intentar obtener usuario inexistente
api_request "GET" "/users/999" "" \
    "Intentar obtener usuario inexistente (debe fallar)"

echo -e "${BLUE}📦 === OPERACIONES CON ITEMS ===${NC}"

# 7. Crear items para usuarios
api_request "POST" "/users/1/items/" \
    '{"nombre": "Servidor Principal", "descripcion": "Servidor de producción para la aplicación web"}' \
    "Crear item para usuario 1 (admin)"

api_request "POST" "/users/2/items/" \
    '{"nombre": "Laptop de Desarrollo", "descripcion": "MacBook Pro para desarrollo"}' \
    "Crear item para usuario 2 (dev)"

api_request "POST" "/users/2/items/" \
    '{"nombre": "Monitor 4K", "descripcion": "Monitor para programación"}' \
    "Crear segundo item para usuario 2"

api_request "POST" "/users/3/items/" \
    '{"nombre": "Dispositivo de Testing", "descripcion": "Tablet para pruebas de UI"}' \
    "Crear item para usuario 3 (test)"

# 8. Intentar crear item para usuario inexistente
api_request "POST" "/users/999/items/" \
    '{"nombre": "Item Huérfano", "descripcion": "Este item no debería crearse"}' \
    "Intentar crear item para usuario inexistente (debe fallar)"

# 9. Listar todos los items
api_request "GET" "/items/" "" \
    "Obtener lista de todos los items"

# 10. Actualizar un item
api_request "PUT" "/items/1" \
    '{"nombre": "Servidor Principal Actualizado", "descripcion": "Servidor de producción con más RAM"}' \
    "Actualizar item con ID 1"

# 11. Intentar actualizar item inexistente
api_request "PUT" "/items/999" \
    '{"nombre": "Item Fantasma", "descripcion": "No existe"}' \
    "Intentar actualizar item inexistente (debe fallar)"

# 12. Eliminar un item
api_request "DELETE" "/items/2" "" \
    "Eliminar item con ID 2"

# 13. Intentar eliminar item inexistente
api_request "DELETE" "/items/999" "" \
    "Intentar eliminar item inexistente (debe fallar)"

# 14. Verificar estado final
echo -e "${BLUE}🔍 === ESTADO FINAL ===${NC}"
api_request "GET" "/users/" "" \
    "Estado final de usuarios"

api_request "GET" "/items/" "" \
    "Estado final de items"

echo -e "${GREEN}🎉 ¡Prueba de API completada!${NC}"
echo ""
echo -e "${BLUE}📊 Resumen:${NC}"
echo "   • Usuarios creados: 3"
echo "   • Items creados: 4"
echo "   • Items eliminados: 1"
echo "   • Errores probados: 5"
echo ""
echo -e "${BLUE}🌐 Documentación automática disponible en:${NC}"
echo "   • Swagger UI: $API_URL/docs"
echo "   • ReDoc: $API_URL/redoc"