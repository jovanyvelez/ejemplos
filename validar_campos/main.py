"""
🎓 PROYECTO EDUCATIVO: VALIDACIÓN DE FORMULARIOS CON FASTAPI Y PYDANTIC

Este proyecto te enseña cómo validar datos de formularios en el backend
de una aplicación web usando FastAPI y Pydantic.

¿Qué aprenderás?
- Cómo crear formularios HTML
- Cómo recibir datos del formulario en el backend
- Cómo validar esos datos usando Pydantic
- Cómo mostrar errores de validación al usuario
- Cómo usar plantillas Jinja2 para renderizar HTML dinámico
"""

# ========== IMPORTACIONES ==========
# Aquí importamos todas las librerías que necesitamos

# 📝 Annotated: Nos permite agregar metadatos a los tipos de datos
# Por ejemplo, podemos especificar que un parámetro viene de un formulario
from typing import Annotated

# 🚨 ValidationError: Esta excepción se lanza cuando Pydantic encuentra datos inválidos
# Es muy importante capturarla para manejar errores de validación
from pydantic import ValidationError

# 🚀 FastAPI: El framework web que usamos
# - FastAPI: La clase principal para crear nuestra aplicación
# - Request: Representa la petición HTTP que llega al servidor
# - Form: Indica que un parámetro viene de un formulario HTML
from fastapi import FastAPI, Request, Form

# 🎨 Jinja2Templates: Nos permite usar plantillas HTML dinámicas
# Con esto podemos insertar datos de Python dentro de nuestro HTML
from fastapi.templating import Jinja2Templates

# 📁 StaticFiles: Nos permite servir archivos estáticos como CSS, imágenes, etc.
from fastapi.staticfiles import StaticFiles 

# 👤 User: Nuestro modelo de datos personalizado (está en modelos_pydantic.py)
# Este modelo define qué datos esperamos del usuario y cómo validarlos
from modelos_pydantic import User

# ========== CONFIGURACIÓN DE LA APLICACIÓN ==========

# 🏗️ Creamos nuestra aplicación FastAPI
# - title: El nombre de nuestra aplicación
# - version: La versión actual
# - description: Una descripción de qué hace nuestra aplicación
app = FastAPI(
    title="📚 Validación de Formularios - Proyecto Educativo", 
    version="1.0.0", 
    description="""Un ejemplo práctico para aprender cómo validar formularios web 
                   usando FastAPI y Pydantic. Perfecto para estudiantes."""
)

# 🎨 Configuramos el motor de plantillas Jinja2
# Esto nos permite crear páginas HTML dinámicas donde podemos insertar
# datos de Python (como mensajes de error) dentro del HTML
templates = Jinja2Templates(directory="templates")

# 📁 Montamos la carpeta de archivos estáticos
# Esto permite que el navegador acceda a nuestros archivos CSS
# Cuando escribas "/static/archivo.css" en HTML, FastAPI buscará en la carpeta "static"
app.mount("/static", StaticFiles(directory="static"), name="static")


# ========== RUTAS DE LA APLICACIÓN ==========

# 🏠 RUTA PRINCIPAL - Muestra el formulario de login
# El decorador @app.get("/") significa que esta función se ejecuta
# cuando alguien visita la página principal de nuestro sitio web
@app.get("/")
async def mostrar_formulario_login(request: Request):
    """
    📄 Esta función muestra la página principal con el formulario de login.
    
    ¿Qué hace?
    1. Recibe la petición del navegador (request)
    2. Renderiza la plantilla "login.html"
    3. Le pasa un diccionario vacío de errores (porque aún no ha habido errores)
    
    Parámetros:
    - request: La petición HTTP que viene del navegador
    
    Retorna:
    - Una página HTML renderizada con el formulario
    """
    # Renderizamos la plantilla login.html
    # - name: el archivo HTML que queremos mostrar
    # - request: la petición del navegador (siempre necesaria)
    # - context: los datos que queremos pasar al HTML (en este caso, errores vacíos)
    return templates.TemplateResponse(
        name="login.html", 
        request=request, 
        context={"errors": {}}
    )

# 📝 RUTA DE PROCESAMIENTO - Valida los datos del formulario
# El decorador @app.post("/login/") significa que esta función se ejecuta
# cuando alguien envía el formulario (método POST) a la URL "/login/"
@app.post("/login/")
async def procesar_login(
    request: Request, 
    email: Annotated[str, Form()],     # El email viene del formulario HTML
    password: Annotated[str, Form()]   # La contraseña viene del formulario HTML
):
    """
    🔍 Esta función procesa y valida los datos enviados desde el formulario.
    
    ¿Qué hace?
    1. Recibe los datos del formulario (email y password)
    2. Intenta crear un objeto User con esos datos (aquí es donde se valida)
    3. Si la validación falla, muestra los errores al usuario
    4. Si la validación es exitosa, muestra una página de éxito
    
    Parámetros:
    - request: La petición HTTP del navegador
    - email: El email que escribió el usuario (viene del input "email")
    - password: La contraseña que escribió el usuario (viene del input "password")
    
    Retorna:
    - Si hay errores: la página del formulario con los errores mostrados
    - Si no hay errores: una página de éxito
    """
    
    # 🛡️ BLOQUE TRY-EXCEPT: Aquí es donde ocurre la magia de la validación
    try:
        # 🔍 VALIDACIÓN: Intentamos crear un objeto User con los datos del formulario
        # Si los datos son válidos, se crea el objeto sin problemas
        # Si los datos son inválidos, Pydantic lanza una ValidationError
        usuario = User(email=email, password=password)
        
        # ✅ Si llegamos aquí, significa que los datos son válidos
        print(f"✅ Usuario válido creado: {usuario.email}")  # Para depuración
        
    except ValidationError as e:
        # 🚨 MANEJO DE ERRORES: Si Pydantic encuentra datos inválidos
        print(f"❌ Error de validación detectado: {e}")  # Para depuración
        
        # 📋 Procesamos los errores para mostrarlos de forma amigable
        errors = {}
        for error in e.errors():
            # error['loc'][0] = el nombre del campo que tiene error (ej: 'email')
            # error['msg'] = el mensaje de error (ej: 'formato de email inválido')
            campo_con_error = error['loc'][0]
            mensaje_error = error['msg']
            errors[campo_con_error] = mensaje_error
            
        print(f"📋 Errores procesados: {errors}")  # Para depuración
        
        # 🔄 Devolvemos el formulario con los errores para que el usuario los vea
        return templates.TemplateResponse(
            request=request, 
            name="login.html", 
            context={"errors": errors}
        )
    
    # 🎉 SI NO HAY ERRORES: Mostramos la página de éxito
    return templates.TemplateResponse(
        "everythingok.html", 
        {"request": request}
    )