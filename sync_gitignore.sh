#!/bin/bash

# Script para sincronizar .gitignore en todos los proyectos
# Ejecutar desde el directorio raíz de ejemplos

set -e

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}🔄 Sincronizando archivos .gitignore${NC}"
echo ""

# Template base para .gitignore de proyectos individuales
create_project_gitignore() {
    local project=$1
    local db_name=$2
    
    cat > "$project/.gitignore" << EOF
# ================================
# GITIGNORE PARA PROYECTO $project
# ================================

# ======================
# PYTHON
# ======================

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*\$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# ======================
# ENTORNOS VIRTUALES
# ======================

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# ======================
# BASES DE DATOS
# ======================

# Base de datos SQLite
*.db
*.sqlite
*.sqlite3
$db_name

# ======================
# ARCHIVOS TEMPORALES
# ======================

# Archivos temporales
temp/
tmp/
*.tmp
*.swp
*.swo
*~
*.bak
*.backup

# ======================
# SISTEMA OPERATIVO
# ======================

# macOS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes

# Windows
ehthumbs.db
Thumbs.db
Desktop.ini

# Linux
*~

# ======================
# IDEs
# ======================

# Visual Studio Code
.vscode/

# PyCharm
.idea/

# Sublime Text
*.sublime-project
*.sublime-workspace

# ======================
# LOGS Y DEBUGGING
# ======================

# Logs
*.log
logs/
log/

# FastAPI/Uvicorn logs
uvicorn.log

# ======================
# ARCHIVOS DE CONFIGURACIÓN
# ======================

# No incluir configuración local (mantener .example)
config.py
config.json
secrets.json

# ======================
# UPLOADS Y MEDIA
# ======================

# Archivos subidos por usuarios
uploads/
media/
user_files/
EOF
    
    echo -e "${GREEN}✅ $project/.gitignore actualizado${NC}"
}

# Actualizar .gitignore para validar_campos
if [ -d "validar_campos" ]; then
    echo -e "${YELLOW}📝 Actualizando validar_campos/.gitignore${NC}"
    create_project_gitignore "validar_campos" "ejemplo.db"
fi

# Actualizar .gitignore para proyecto_api_base_datos
if [ -d "proyecto_api_base_datos" ]; then
    echo -e "${YELLOW}📝 Actualizando proyecto_api_base_datos/.gitignore${NC}"
    create_project_gitignore "proyecto_api_base_datos" "sql_app_ejemplo.db"
fi

# Actualizar .gitignore para proyecto_web_base_datos
if [ -d "proyecto_web_base_datos" ]; then
    echo -e "${YELLOW}📝 Actualizando proyecto_web_base_datos/.gitignore${NC}"
    create_project_gitignore "proyecto_web_base_datos" "web_app.db"
fi

# Verificar que el .gitignore principal existe
if [ ! -f ".gitignore" ]; then
    echo -e "${YELLOW}⚠️  .gitignore principal no encontrado${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}📊 === RESUMEN ===${NC}"
echo -e "${GREEN}✅ .gitignore principal configurado${NC}"

# Contar cuántos .gitignore fueron actualizados
count=0
for project in "validar_campos" "proyecto_api_base_datos" "proyecto_web_base_datos"; do
    if [ -d "$project" ] && [ -f "$project/.gitignore" ]; then
        echo -e "${GREEN}✅ $project/.gitignore configurado${NC}"
        ((count++))
    fi
done

echo ""
echo -e "${BLUE}📋 === ARCHIVOS PRINCIPALES IGNORADOS ===${NC}"
echo "• __pycache__/ y *.pyc (Python compilado)"
echo "• .venv/ (Entornos virtuales)"
echo "• *.db, *.sqlite (Bases de datos)"
echo "• .env (Variables de entorno)"
echo "• *.log (Archivos de log)"
echo "• .vscode/, .idea/ (Configuración IDEs)"
echo "• .DS_Store, Thumbs.db (Sistema operativo)"
echo "• temp/, tmp/ (Archivos temporales)"

echo ""
echo -e "${BLUE}💡 === COMANDOS ÚTILES ===${NC}"
echo "• Ver archivos ignorados: git status --ignored"
echo "• Limpiar cache Git: git rm -r --cached . && git add ."
echo "• Verificar estado: git status"

echo ""
echo -e "${GREEN}🎉 ¡Sincronización de .gitignore completada!${NC}"
echo -e "${GREEN}Total de proyectos configurados: $count${NC}"