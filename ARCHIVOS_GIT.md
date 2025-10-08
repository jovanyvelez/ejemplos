# Archivos a Incluir en Git

Este documento explica qué archivos **SÍ deben** estar en el repositorio para que el proyecto funcione correctamente.

## ✅ Archivos ESENCIALES que deben estar en Git

### 📁 Directorio Raíz (`ejemplos/`)
```
✅ README.md                    # Documentación principal
✅ INICIO_RAPIDO.md             # Guía rápida
✅ ROADMAP_TECNOLOGIAS.md       # Stack tecnológico
✅ ESTRUCTURA_ARCHIVOS.md       # Este archivo
✅ ARCHIVOS_GIT.md             # Guía de archivos Git
✅ .gitignore                   # Configuración Git
✅ setup.sh                     # Script de configuración
```

### 🔰 Proyecto: `validar_campos/`
```
✅ main.py                      # Aplicación principal
✅ modelos_pydantic.py          # Modelos de validación
✅ ejemplos_practica.py         # Ejemplos adicionales
✅ iniciar_proyecto.py          # Script de inicio
✅ README.md                    # Documentación
✅ pyproject.toml               # Dependencias
✅ templates/
   ✅ login.html               # Formulario de login
   ✅ everythingok.html        # Página de éxito
✅ static/
   ✅ form_styles.css          # Estilos CSS
   ✅ flujo.png                # Diagrama de flujo
```

### 🚀 Proyecto: `proyecto_api_base_datos/`
```
✅ main.py                      # Configuración FastAPI
✅ users.py                     # Rutas de la API
✅ database.py                  # Configuración BD
✅ models.py                    # Esquemas de tablas
✅ crud.py                      # Operaciones CRUD
✅ schemas.py                   # Modelos Pydantic
✅ README.md                    # Documentación completa
✅ EJEMPLOS.md                  # Ejemplos de uso
✅ API_VS_WEB.md               # Comparación educativa
✅ EJERCICIOS.md               # Ejercicios progresivos
✅ pyproject.toml              # Dependencias
✅ .env.example                # Configuración ejemplo
✅ .gitignore                  # Archivos a ignorar
✅ test_api.sh                 # Script de pruebas
```

### 🌐 Proyecto: `proyecto_web_base_datos/`
```
✅ main.py                      # Aplicación web
✅ database.py                  # Configuración BD
✅ models.py                    # Esquemas BD
✅ crud.py                      # Operaciones CRUD
✅ schemas.py                   # Modelos Pydantic
✅ README.md                    # Documentación
✅ pyproject.toml              # Dependencias
✅ .env.example                # Configuración ejemplo
✅ .gitignore                  # Archivos a ignorar
✅ populate_db.py              # Datos de ejemplo
✅ templates/
   ✅ base.html                # Layout base
   ✅ index.html               # Página inicio
   ✅ users.html               # Lista usuarios
   ✅ user_form.html           # Formulario usuario
   ✅ user_detail.html         # Detalle usuario
   ✅ items.html               # Lista items
   ✅ item_form.html           # Formulario item
✅ static/
   ✅ style.css                # CSS profesional
```

## ❌ Archivos que NO deben estar en Git

### 🚫 Archivos Generados Automáticamente
```
❌ __pycache__/                 # Cache de Python
❌ *.pyc                        # Python compilado
❌ *.pyo                        # Python optimizado
❌ .pytest_cache/              # Cache de pytest
❌ htmlcov/                    # Reportes de coverage
```

### 🚫 Entornos y Configuración Local
```
❌ .venv/                      # Entorno virtual
❌ .env                        # Variables de entorno
❌ config.json                 # Configuración local
❌ secrets.json                # Secretos y claves
```

### 🚫 Bases de Datos
```
❌ *.db                        # Bases de datos SQLite
❌ *.sqlite                    # Archivos SQLite
❌ *.sqlite3                   # SQLite3
❌ sql_app_ejemplo.db          # BD del proyecto API
❌ web_app.db                  # BD del proyecto web
```

### 🚫 Archivos Temporales
```
❌ *.log                       # Logs de aplicación
❌ *.tmp                       # Archivos temporales
❌ *.swp                       # Archivos Vim
❌ .DS_Store                   # Archivos macOS
❌ Thumbs.db                   # Archivos Windows
```

### 🚫 IDEs y Editores
```
❌ .vscode/                    # Configuración VS Code
❌ .idea/                      # Configuración PyCharm
❌ *.sublime-workspace         # Sublime Text
```

### 🚫 Archivos de Build y Distribución
```
❌ build/                      # Archivos de build
❌ dist/                       # Distribución
❌ *.egg-info/                 # Info de paquetes
```

## 🔧 Comandos Git Útiles

### Verificar qué archivos están siendo ignorados
```bash
git status --ignored
```

### Ver qué archivos están en el staging area
```bash
git status
```

### Agregar archivos específicos
```bash
git add README.md
git add *.py
git add templates/
```

### Agregar todos los archivos permitidos
```bash
git add .
```

### Ver diferencias antes de commit
```bash
git diff --cached
```

## 📋 Checklist antes de hacer commit

### ✅ Verificar que tienes estos archivos:
- [ ] Todos los archivos `.py` necesarios
- [ ] `README.md` actualizado
- [ ] `pyproject.toml` con dependencias correctas
- [ ] Templates HTML necesarios
- [ ] Archivos CSS/estáticos
- [ ] Scripts de configuración (`.sh`)
- [ ] Archivos de ejemplo (`.example`)

### ❌ Verificar que NO tienes estos archivos:
- [ ] Archivos `.db` o `.sqlite`
- [ ] Directorio `.venv/`
- [ ] Archivos `.env` (solo `.env.example`)
- [ ] Directorio `__pycache__/`
- [ ] Archivos `.log`
- [ ] Configuración de IDEs (`.vscode/`, `.idea/`)

## 🚀 Flujo de Trabajo Recomendado

### 1. Antes de empezar a trabajar
```bash
# Actualizar desde remoto
git pull origin main

# Verificar estado
git status
```

### 2. Después de hacer cambios
```bash
# Ver qué cambió
git status
git diff

# Agregar archivos específicos
git add archivo_modificado.py
git add README.md

# O agregar todos los cambios válidos
git add .
```

### 3. Antes de hacer commit
```bash
# Verificar qué se va a commitear
git status

# Verificar que no hay archivos no deseados
git status --ignored

# Hacer commit
git commit -m "Descripción clara de los cambios"
```

### 4. Enviar al repositorio
```bash
git push origin main
```

## 🔍 Solución de Problemas

### Problema: "Archivos no deseados en el repositorio"
```bash
# Remover archivo del repositorio pero mantener local
git rm --cached archivo.db

# Remover directorio del repositorio
git rm -r --cached __pycache__/

# Commit los cambios
git commit -m "Remove unwanted files"
```

### Problema: ".gitignore no funciona"
```bash
# Limpiar cache de Git
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

### Problema: "Archivo grande no se puede subir"
```bash
# Verificar tamaño de archivos
find . -type f -size +10M

# Si es necesario, usar Git LFS para archivos grandes
git lfs track "*.db"
```

## 📊 Tamaños Recomendados

| Tipo de Archivo | Tamaño Máximo | Acción |
|------------------|---------------|---------|
| **Código Python** | < 1MB | ✅ Incluir |
| **Templates HTML** | < 100KB | ✅ Incluir |
| **CSS** | < 100KB | ✅ Incluir |
| **Imágenes** | < 1MB | ✅ Incluir |
| **Base de datos** | Cualquiera | ❌ Ignorar |
| **Logs** | Cualquiera | ❌ Ignorar |

## 💡 Mejores Prácticas

1. **Commits frecuentes**: Mejor muchos commits pequeños que uno grande
2. **Mensajes descriptivos**: Explica QUÉ y POR QUÉ cambiaste algo
3. **Review antes de commit**: Siempre verifica con `git status` y `git diff`
4. **Mantén .gitignore actualizado**: Agrega nuevos patrones cuando sea necesario
5. **No commitees secretos**: Nunca incluyas passwords o API keys

¡Seguir estas guías mantendrá tu repositorio limpio y profesional! 🧹✨