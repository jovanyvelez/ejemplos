#!/bin/bash

# Script de configuración para todos los proyectos de ejemplo
# Ejecutar desde el directorio raíz de ejemplos

set -e  # Salir si hay errores

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    EJEMPLOS FASTAPI                         ║"
echo "║              Configuración Automática                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar Python
echo -e "${YELLOW}🐍 Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 no encontrado. Instala Python 3.8 o superior.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}✅ Python $PYTHON_VERSION encontrado${NC}"

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}📦 Creando entorno virtual...${NC}"
    python3 -m venv .venv
    echo -e "${GREEN}✅ Entorno virtual creado${NC}"
else
    echo -e "${GREEN}✅ Entorno virtual ya existe${NC}"
fi

# Activar entorno virtual
echo -e "${YELLOW}🔌 Activando entorno virtual...${NC}"
source .venv/bin/activate

# Instalar dependencias para todos los proyectos
echo -e "${YELLOW}📥 Instalando dependencias comunes...${NC}"

# Dependencias base
pip install --upgrade pip > /dev/null 2>&1
pip install "fastapi[standard]>=0.118.0" > /dev/null 2>&1
pip install "sqlalchemy>=2.0.43" > /dev/null 2>&1
pip install "jinja2>=3.1.2" > /dev/null 2>&1
pip install "python-multipart>=0.0.6" > /dev/null 2>&1

# Dependencias adicionales para desarrollo
pip install requests > /dev/null 2>&1
pip install pytest > /dev/null 2>&1
pip install httpx > /dev/null 2>&1

echo -e "${GREEN}✅ Dependencias instaladas${NC}"

# Verificar estructura de proyectos
echo -e "${YELLOW}📁 Verificando estructura de proyectos...${NC}"

projects=("validar_campos" "proyecto_api_base_datos" "proyecto_web_base_datos")
for project in "${projects[@]}"; do
    if [ -d "$project" ]; then
        echo -e "${GREEN}✅ $project encontrado${NC}"
        
        # Verificar archivo main.py
        if [ -f "$project/main.py" ]; then
            echo -e "   └─ main.py ✅"
        else
            echo -e "   └─ main.py ${RED}❌${NC}"
        fi
        
        # Verificar README
        if [ -f "$project/README.md" ]; then
            echo -e "   └─ README.md ✅"
        else
            echo -e "   └─ README.md ${YELLOW}⚠️${NC}"
        fi
    else
        echo -e "${RED}❌ $project no encontrado${NC}"
    fi
done

# Función para probar un proyecto
test_project() {
    local project=$1
    local port=$2
    
    echo -e "${YELLOW}🧪 Probando $project...${NC}"
    
    if [ ! -f "$project/main.py" ]; then
        echo -e "${RED}❌ main.py no encontrado en $project${NC}"
        return 1
    fi
    
    # Probar importación
    cd "$project"
    if python3 -c "import main" 2>/dev/null; then
        echo -e "${GREEN}✅ $project: Importación exitosa${NC}"
    else
        echo -e "${RED}❌ $project: Error de importación${NC}"
    fi
    cd ..
}

# Probar proyectos
echo -e "\n${BLUE}🧪 === PRUEBAS DE PROYECTOS ===${NC}"
for project in "${projects[@]}"; do
    if [ -d "$project" ]; then
        test_project "$project"
    fi
done

# Crear scripts de inicio rápido
echo -e "\n${YELLOW}🚀 Creando scripts de inicio rápido...${NC}"

# Script para validar_campos
if [ -d "validar_campos" ]; then
cat > validar_campos/start.sh << 'EOF'
#!/bin/bash
echo "🚀 Iniciando Validación de Campos..."
source ../.venv/bin/activate
python main.py
EOF
chmod +x validar_campos/start.sh
echo -e "${GREEN}✅ Script para validar_campos creado${NC}"
fi

# Script para proyecto_api_base_datos
if [ -d "proyecto_api_base_datos" ]; then
cat > proyecto_api_base_datos/start.sh << 'EOF'
#!/bin/bash
echo "🚀 Iniciando API Base de Datos..."
source ../.venv/bin/activate
python main.py
EOF
chmod +x proyecto_api_base_datos/start.sh
echo -e "${GREEN}✅ Script para proyecto_api_base_datos creado${NC}"
fi

# Script para proyecto_web_base_datos
if [ -d "proyecto_web_base_datos" ] && [ ! -f "proyecto_web_base_datos/start.sh" ]; then
cat > proyecto_web_base_datos/start.sh << 'EOF'
#!/bin/bash
echo "🚀 Iniciando Aplicación Web..."
source ../.venv/bin/activate
python main.py
EOF
chmod +x proyecto_web_base_datos/start.sh
echo -e "${GREEN}✅ Script para proyecto_web_base_datos creado${NC}"
fi

# Mostrar resumen
echo -e "\n${BLUE}📊 === RESUMEN DE CONFIGURACIÓN ===${NC}"
echo -e "${GREEN}✅ Entorno virtual configurado${NC}"
echo -e "${GREEN}✅ Dependencias instaladas${NC}"
echo -e "${GREEN}✅ Proyectos verificados${NC}"
echo -e "${GREEN}✅ Scripts de inicio creados${NC}"

echo -e "\n${BLUE}🎯 === CÓMO USAR ===${NC}"
echo -e "1. Para activar el entorno virtual:"
echo -e "   ${YELLOW}source .venv/bin/activate${NC}"
echo -e ""
echo -e "2. Para ejecutar un proyecto:"
echo -e "   ${YELLOW}cd [nombre_proyecto]${NC}"
echo -e "   ${YELLOW}./start.sh${NC}"
echo -e ""
echo -e "3. Proyectos disponibles:"
for project in "${projects[@]}"; do
    if [ -d "$project" ]; then
        echo -e "   ${GREEN}✅ $project${NC}"
    else
        echo -e "   ${RED}❌ $project${NC}"
    fi
done

echo -e "\n${BLUE}📚 === DOCUMENTACIÓN ===${NC}"
echo -e "• README.md principal - Guía completa"
echo -e "• INICIO_RAPIDO.md - Guía rápida"
echo -e "• ROADMAP_TECNOLOGIAS.md - Stack tecnológico"
echo -e "• [proyecto]/README.md - Documentación específica"

echo -e "\n${BLUE}🌐 === PUERTOS POR DEFECTO ===${NC}"
echo -e "• validar_campos: http://localhost:8000"
echo -e "• proyecto_api_base_datos: http://localhost:8000"
echo -e "• proyecto_web_base_datos: http://localhost:8000"
echo -e ""
echo -e "${YELLOW}💡 Ejecuta solo un proyecto a la vez o cambia el puerto${NC}"

echo -e "\n${GREEN}🎉 ¡Configuración completada! ¡Listo para aprender!${NC}"