# Guía Rápida de Inicio

Esta es una guía condensada para empezar rápidamente con cualquiera de los proyectos de ejemplo.

## ⚡ Inicio Rápido

### 1. Preparación del Entorno (Una sola vez)

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno (Linux/Mac)
source .venv/bin/activate

# Activar entorno (Windows)
.venv\Scripts\activate
```

### 2. Ejecutar Proyecto Específico

#### 🔰 Validación de Campos (Principiante)
```bash
cd validar_campos
pip install "fastapi[standard]" jinja2 python-multipart
python main.py
# Visita: http://localhost:8000
```

#### 🚀 API Base de Datos (Intermedio)
```bash
cd proyecto_api_base_datos
pip install "fastapi[standard]" sqlalchemy
python main.py
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

#### 🌐 Aplicación Web (Avanzado)
```bash
cd proyecto_web_base_datos
pip install "fastapi[standard]" sqlalchemy jinja2 python-multipart
python main.py
# Web: http://localhost:8000
```

## 🧪 Pruebas Rápidas

### API (proyecto_api_base_datos)
```bash
# Crear usuario
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'

# Listar usuarios
curl -X GET "http://localhost:8000/users/"
```

### Web App (proyecto_web_base_datos)
1. Ve a http://localhost:8000
2. Navega a "Usuarios"
3. Crea un nuevo usuario
4. Crea items para el usuario

## 🔧 Solución de Problemas Comunes

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError` | `pip install [paquete]` |
| `Port 8000 in use` | Usar `--port 8001` |
| `Permission denied` | `chmod +x script.sh` |
| CSS no carga | Verificar directorio `static/` |

## 📚 Documentación Completa

Para más detalles, ver:
- `README.md` - Guía completa
- `proyecto_*/README.md` - Documentación específica
- `proyecto_*/EJEMPLOS.md` - Ejemplos de uso
- `proyecto_*/EJERCICIOS.md` - Práctica adicional