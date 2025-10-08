#!/bin/bash

# Script para verificar la configuración del .gitignore
# Ejecutar desde el directorio raíz de ejemplos

set -e

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                VERIFICACIÓN DE .GITIGNORE                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar que existe .gitignore principal
if [ ! -f ".gitignore" ]; then
    echo -e "${RED}❌ .gitignore principal no encontrado${NC}"
    exit 1
fi

echo -e "${GREEN}✅ .gitignore principal encontrado${NC}"

# Verificar .gitignore en cada proyecto
projects=("validar_campos" "proyecto_api_base_datos" "proyecto_web_base_datos")
for project in "${projects[@]}"; do
    if [ -d "$project" ]; then
        if [ -f "$project/.gitignore" ]; then
            echo -e "${GREEN}✅ $project/.gitignore encontrado${NC}"
        else
            echo -e "${RED}❌ $project/.gitignore no encontrado${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Directorio $project no encontrado${NC}"
    fi
done

echo ""
echo -e "${BLUE}🔍 === ARCHIVOS QUE DEBEN SER IGNORADOS ===${NC}"

# Buscar archivos que deberían estar ignorados
ignored_found=0

# Buscar __pycache__
pycache_dirs=$(find . -name "__pycache__" -type d 2>/dev/null | wc -l)
if [ $pycache_dirs -gt 0 ]; then
    echo -e "${GREEN}📁 $pycache_dirs directorios __pycache__ encontrados (serán ignorados)${NC}"
    ((ignored_found++))
fi

# Buscar .venv
venv_dirs=$(find . -name ".venv" -type d 2>/dev/null | wc -l)
if [ $venv_dirs -gt 0 ]; then
    echo -e "${GREEN}🐍 $venv_dirs directorios .venv encontrados (serán ignorados)${NC}"
    ((ignored_found++))
fi

# Buscar archivos .db
db_files=$(find . -name "*.db" -type f 2>/dev/null | wc -l)
if [ $db_files -gt 0 ]; then
    echo -e "${GREEN}🗄️  $db_files archivos .db encontrados (serán ignorados)${NC}"
    ((ignored_found++))
fi

# Buscar archivos .env (no .example)
env_files=$(find . -name ".env" -not -name "*.example" -type f 2>/dev/null | wc -l)
if [ $env_files -gt 0 ]; then
    echo -e "${GREEN}⚙️  $env_files archivos .env encontrados (serán ignorados)${NC}"
    ((ignored_found++))
fi

# Buscar archivos de log
log_files=$(find . -name "*.log" -type f 2>/dev/null | wc -l)
if [ $log_files -gt 0 ]; then
    echo -e "${GREEN}📝 $log_files archivos .log encontrados (serán ignorados)${NC}"
    ((ignored_found++))
fi

if [ $ignored_found -eq 0 ]; then
    echo -e "${YELLOW}ℹ️  No se encontraron archivos que necesiten ser ignorados${NC}"
fi

echo ""
echo -e "${BLUE}📊 === ESTADO DE GIT ===${NC}"

# Verificar si estamos en un repositorio Git
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}⚠️  No es un repositorio Git. Para inicializar:${NC}"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
else
    echo -e "${GREEN}✅ Repositorio Git inicializado${NC}"
    
    # Mostrar archivos ignorados
    ignored_count=$(git status --ignored --porcelain | grep "^!!" | wc -l)
    if [ $ignored_count -gt 0 ]; then
        echo -e "${GREEN}🚫 $ignored_count archivos/directorios siendo ignorados por Git${NC}"
    else
        echo -e "${YELLOW}ℹ️  No hay archivos siendo ignorados actualmente${NC}"
    fi
    
    # Mostrar archivos sin seguimiento
    untracked_count=$(git status --porcelain | grep "^??" | wc -l)
    if [ $untracked_count -gt 0 ]; then
        echo -e "${BLUE}📄 $untracked_count archivos sin seguimiento (listos para añadir)${NC}"
    fi
fi

echo ""
echo -e "${BLUE}📋 === ARCHIVOS IMPORTANTES A INCLUIR ===${NC}"
echo -e "${GREEN}✅ Código Python (*.py)${NC}"
echo -e "${GREEN}✅ Templates HTML (templates/*.html)${NC}"
echo -e "${GREEN}✅ Estilos CSS (static/*.css)${NC}"
echo -e "${GREEN}✅ Documentación (*.md)${NC}"
echo -e "${GREEN}✅ Configuración (pyproject.toml, .env.example)${NC}"
echo -e "${GREEN}✅ Scripts (*.sh)${NC}"

echo ""
echo -e "${BLUE}🚫 === ARCHIVOS A NO INCLUIR ===${NC}"
echo -e "${RED}❌ Entornos virtuales (.venv/)${NC}"
echo -e "${RED}❌ Cache Python (__pycache__/)${NC}"
echo -e "${RED}❌ Bases de datos (*.db, *.sqlite)${NC}"
echo -e "${RED}❌ Variables de entorno (.env)${NC}"
echo -e "${RED}❌ Logs (*.log)${NC}"
echo -e "${RED}❌ Configuración IDEs (.vscode/, .idea/)${NC}"

echo ""
echo -e "${BLUE}🔧 === COMANDOS ÚTILES ===${NC}"
echo "• Ver archivos ignorados:"
echo "  ${YELLOW}git status --ignored${NC}"
echo ""
echo "• Limpiar cache de Git (si .gitignore no funciona):"
echo "  ${YELLOW}git rm -r --cached .${NC}"
echo "  ${YELLOW}git add .${NC}"
echo ""
echo "• Añadir archivos al repositorio:"
echo "  ${YELLOW}git add .${NC}"
echo "  ${YELLOW}git commit -m 'Descripción del commit'${NC}"
echo ""
echo "• Verificar qué se va a commitear:"
echo "  ${YELLOW}git status${NC}"
echo "  ${YELLOW}git diff --cached${NC}"

echo ""
if [ $ignored_found -gt 0 ]; then
    echo -e "${GREEN}🎉 ¡Configuración de .gitignore exitosa!${NC}"
    echo -e "${GREEN}Los archivos innecesarios serán ignorados automáticamente.${NC}"
else
    echo -e "${BLUE}ℹ️  Configuración de .gitignore completada.${NC}"
    echo -e "${BLUE}Cuando generes archivos de desarrollo, serán ignorados automáticamente.${NC}"
fi