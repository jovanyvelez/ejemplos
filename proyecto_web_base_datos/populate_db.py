"""
Script para poblar la base de datos con datos de ejemplo
Ejecutar después de iniciar la aplicación por primera vez
"""

import requests
import time

BASE_URL = "http://localhost:8000"

def create_sample_users():
    """Crear usuarios de ejemplo"""
    users_data = [
        {"email": "juan@ejemplo.com", "password": "password123"},
        {"email": "maria@ejemplo.com", "password": "password123"},
        {"email": "pedro@ejemplo.com", "password": "password123"},
        {"email": "ana@ejemplo.com", "password": "password123"},
    ]
    
    print("🧑‍💼 Creando usuarios de ejemplo...")
    created_users = []
    
    for user_data in users_data:
        try:
            response = requests.post(f"{BASE_URL}/users/create", data=user_data)
            if response.status_code == 303:  # Redirect after successful creation
                print(f"✅ Usuario creado: {user_data['email']}")
                created_users.append(user_data)
            else:
                print(f"❌ Error creando usuario {user_data['email']}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error de conexión creando usuario {user_data['email']}: {e}")
    
    return created_users

def create_sample_items():
    """Crear items de ejemplo"""
    # Obtener lista de usuarios para asignar items
    items_data = [
        {"nombre": "Laptop Dell", "descripcion": "Laptop para trabajo", "propietario_id": 1},
        {"nombre": "Mouse inalámbrico", "descripcion": "Mouse Bluetooth", "propietario_id": 1},
        {"nombre": "Teclado mecánico", "descripcion": "Teclado gaming RGB", "propietario_id": 2},
        {"nombre": "Monitor 24\"", "descripcion": "Monitor Full HD", "propietario_id": 2},
        {"nombre": "Tablet Android", "descripcion": "Tablet para lectura", "propietario_id": 3},
        {"nombre": "Auriculares", "descripcion": "Auriculares con cancelación de ruido", "propietario_id": 3},
        {"nombre": "Smartphone", "descripcion": "Teléfono móvil último modelo", "propietario_id": 4},
        {"nombre": "Cargador portátil", "descripcion": "Power bank 20000mAh", "propietario_id": 4},
    ]
    
    print("📦 Creando items de ejemplo...")
    
    for item_data in items_data:
        try:
            response = requests.post(f"{BASE_URL}/items/create", data=item_data)
            if response.status_code == 303:  # Redirect after successful creation
                print(f"✅ Item creado: {item_data['nombre']}")
            else:
                print(f"❌ Error creando item {item_data['nombre']}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error de conexión creando item {item_data['nombre']}: {e}")

def main():
    print("🌟 Poblando la base de datos con datos de ejemplo...")
    print("⚠️  Asegúrate de que la aplicación esté ejecutándose en http://localhost:8000")
    print("")
    
    # Esperar un poco para asegurar que la aplicación esté lista
    time.sleep(2)
    
    # Crear usuarios
    users = create_sample_users()
    
    if users:
        print("")
        # Crear items
        create_sample_items()
        
        print("")
        print("🎉 ¡Datos de ejemplo creados exitosamente!")
        print(f"🌐 Visita {BASE_URL} para ver la aplicación")
        print("")
        print("👥 Usuarios creados:")
        for user in users:
            print(f"   - {user['email']}")
        print("")
        print("📦 Items creados para cada usuario")
    else:
        print("❌ No se pudieron crear usuarios. Verifica que la aplicación esté ejecutándose.")

if __name__ == "__main__":
    main()