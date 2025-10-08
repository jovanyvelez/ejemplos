#!/bin/bash

# Script para iniciar la aplicación web
echo "🚀 Iniciando Aplicación Web CRUD..."
echo "📁 Directorio: $(pwd)"
echo ""

# Verificar si existe el entorno virtual
if [ ! -d ".venv" ]; then
    echo "⚠️  No se encontró entorno virtual. Creando uno nuevo..."
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
else
    echo "✅ Activando entorno virtual existente..."
    source .venv/bin/activate
fi

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install "fastapi[standard]>=0.118.0" "sqlalchemy>=2.0.43" "jinja2>=3.1.2" "python-multipart>=0.0.6"

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "⚙️  Creando archivo de configuración .env..."
    cp .env.example .env
fi

echo ""
echo "🎉 ¡Listo para iniciar!"
echo "🌐 La aplicación estará disponible en: http://localhost:8000"
echo ""

# Iniciar la aplicación
python main.py