#!/usr/bin/env python3
"""
🚀 SCRIPT DE INICIO FÁCIL PARA ESTUDIANTES
==========================================

Este script te ayuda a ejecutar el proyecto de forma sencilla
y te da información útil sobre cómo usar la aplicación.

¡Solo ejecuta este archivo y sigue las instrucciones!
"""

import subprocess
import sys
import webbrowser
import time
from pathlib import Path


def imprimir_banner():
    """Imprime un banner bonito de bienvenida"""
    print("""
    🎓========================================🎓
    📚  PROYECTO EDUCATIVO: VALIDACIÓN WEB   📚
    🎓========================================🎓
    
    ¡Bienvenido al proyecto más completo para
    aprender validación de formularios web!
    
    🎯 Tecnologías que aprenderás:
    • FastAPI - Framework web moderno
    • Pydantic - Validación automática  
    • Jinja2 - Plantillas HTML dinámicas
    • HTML/CSS - Frontend responsivo
    """)


def verificar_dependencias():
    """Verifica si están instaladas las dependencias necesarias"""
    print("🔍 Verificando dependencias...")
    
    dependencias = ["fastapi", "uvicorn", "pydantic", "jinja2"]
    faltantes = []
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} - NO ENCONTRADO")
            faltantes.append(dep)
    
    if faltantes:
        print(f"\n🚨 Faltan dependencias: {', '.join(faltantes)}")
        print("💡 Ejecuta estos comandos:")
        print("   python -m venv venv")
        print("   source venv/bin/activate  # En macOS/Linux")
        print("   venv\\Scripts\\activate     # En Windows")
        print('   pip install "fastapi[standard]"')
        return False
    
    print("✅ Todas las dependencias están instaladas!")
    return True


def mostrar_casos_prueba():
    """Muestra casos de prueba para que los estudiantes experimenten"""
    print("""
    🧪 CASOS DE PRUEBA PARA EXPERIMENTAR:
    ====================================
    
    ✅ CASOS EXITOSOS (deberían funcionar):
    • Email: estudiante@colegio.edu
    • Contraseña: mipasword123
    
    ❌ CASOS CON ERRORES (para ver validación):
    • Email sin @: usuario.com
    • Email vacío: (no escribas nada)
    • Contraseña corta: 123
    • Contraseña vacía: (no escribas nada)
    
    🎯 ¡Prueba todos estos casos para ver cómo
       funciona la validación en tiempo real!
    """)


def mostrar_archivos_importantes():
    """Muestra los archivos importantes del proyecto"""
    print("""
    📁 ARCHIVOS IMPORTANTES PARA REVISAR:
    ====================================
    
    🏗️  main.py              - Aplicación principal FastAPI
    🛡️  modelos_pydantic.py  - Validaciones y modelos de datos  
    🎨  templates/login.html  - Formulario HTML con Jinja2
    🎉  templates/everythingok.html - Página de éxito
    🎨  static/form_styles.css - Estilos CSS del formulario
    📚  README.md             - Documentación completa
    🧪  ejemplos_practica.py  - Ejemplos adicionales para practicar
    
    💡 ¡Abre estos archivos en tu editor y léelos!
       Están llenos de comentarios educativos.
    """)


def ejecutar_servidor():
    """Ejecuta el servidor FastAPI usando el comando moderno fastapi dev"""
    print("🚀 Iniciando servidor FastAPI...")
    print("⏳ Esto puede tomar unos segundos...")
    
    try:
        # Intentar usar el comando moderno fastapi dev
        proceso = subprocess.Popen([
            "fastapi", "dev", "main.py", "--port", "8000"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Esperar un momento para que el servidor inicie
        time.sleep(3)
        
        # Verificar si el proceso sigue corriendo
        if proceso.poll() is None:
            print("✅ ¡Servidor iniciado correctamente!")
            print("🌐 Aplicación disponible en: http://localhost:8000")
            
            # Preguntar si quiere abrir el navegador
            respuesta = input("\n🔗 ¿Quieres abrir la aplicación en tu navegador? (s/n): ")
            if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
                print("🌐 Abriendo navegador...")
                webbrowser.open("http://localhost:8000")
            
            print("""
            🎮 CONTROLES DEL SERVIDOR:
            • Para parar el servidor: Ctrl+C
            • Para ver logs: mira esta terminal  
            • Para recargar: guarda cualquier archivo Python
            • Comando usado: fastapi dev main.py
            
            📱 CÓMO USAR LA APLICACIÓN:
            1. Ve a http://localhost:8000 en tu navegador
            2. Prueba los casos de error y éxito
            3. Observa los mensajes de validación
            4. ¡Experimenta y aprende!
            """)
            
            try:
                # Esperar a que el usuario termine
                proceso.wait()
            except KeyboardInterrupt:
                print("\n🛑 Deteniendo servidor...")
                proceso.terminate()
                print("✅ Servidor detenido correctamente.")
        
        else:
            # Si fastapi dev falla, intentar con uvicorn como respaldo
            print("⚠️ fastapi dev no disponible, usando uvicorn como respaldo...")
            ejecutar_con_uvicorn()
            
    except FileNotFoundError:
        print("⚠️ Comando 'fastapi' no encontrado, usando uvicorn como respaldo...")
        ejecutar_con_uvicorn()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        print("💡 Intentando con uvicorn como respaldo...")
        ejecutar_con_uvicorn()


def ejecutar_con_uvicorn():
    """Función de respaldo usando uvicorn directamente"""
    try:
        proceso = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "main:app", "--reload", "--port", "8000"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        time.sleep(3)
        
        if proceso.poll() is None:
            print("✅ ¡Servidor iniciado con uvicorn!")
            print("🌐 Aplicación disponible en: http://localhost:8000")
            
            respuesta = input("\n🔗 ¿Quieres abrir la aplicación en tu navegador? (s/n): ")
            if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
                print("🌐 Abriendo navegador...")
                webbrowser.open("http://localhost:8000")
            
            try:
                proceso.wait()
            except KeyboardInterrupt:
                print("\n🛑 Deteniendo servidor...")
                proceso.terminate()
                print("✅ Servidor detenido correctamente.")
        else:
            stdout, stderr = proceso.communicate()
            print(f"❌ Error al iniciar el servidor:")
            print(f"Salida: {stdout}")
            print(f"Error: {stderr}")
            
    except Exception as e:
        print(f"❌ Error con uvicorn: {e}")
        print("💡 Verifica que FastAPI esté instalado: pip install 'fastapi[standard]'")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("""
    🎮 ¿QUÉ QUIERES HACER?
    =====================
    
    1. 🚀 Ejecutar la aplicación web
    2. 🧪 Ver casos de prueba
    3. 📁 Ver archivos importantes
    4. 📚 Abrir documentación (README)
    5. 🏃 Ejecutar ejemplos de práctica
    6. ❌ Salir
    """)


def main():
    """Función principal"""
    imprimir_banner()
    
    # Verificar que estamos en el directorio correcto
    if not Path("main.py").exists():
        print("❌ Error: No se encuentra main.py")
        print("💡 Asegúrate de ejecutar este script desde la carpeta del proyecto")
        return
    
    # Verificar dependencias
    if not verificar_dependencias():
        return
    
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción (1-6): ").strip()
        
        if opcion == "1":
            ejecutar_servidor()
        elif opcion == "2":
            mostrar_casos_prueba()
        elif opcion == "3":
            mostrar_archivos_importantes()
        elif opcion == "4":
            print("📚 Abriendo README.md...")
            if Path("README.md").exists():
                try:
                    if sys.platform.startswith('darwin'):  # macOS
                        subprocess.run(["open", "README.md"])
                    elif sys.platform.startswith('linux'):  # Linux
                        subprocess.run(["xdg-open", "README.md"])
                    elif sys.platform.startswith('win'):    # Windows
                        subprocess.run(["start", "README.md"], shell=True)
                    else:
                        print("📖 Por favor abre README.md manualmente en tu editor")
                except:
                    print("📖 Por favor abre README.md manualmente en tu editor")
            else:
                print("❌ README.md no encontrado")
        elif opcion == "5":
            if Path("ejemplos_practica.py").exists():
                print("🧪 Ejecutando ejemplos de práctica...")
                subprocess.run([sys.executable, "ejemplos_practica.py"])
            else:
                print("❌ ejemplos_practica.py no encontrado")
        elif opcion == "6":
            print("👋 ¡Hasta luego! ¡Sigue aprendiendo!")
            break
        else:
            print("❌ Opción no válida. Elige un número del 1 al 6.")
        
        input("\n⏎ Presiona Enter para continuar...")
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()