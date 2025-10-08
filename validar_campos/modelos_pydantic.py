
"""
🎓 MODELOS PYDANTIC - VALIDACIÓN DE DATOS

Este archivo define cómo deben ser los datos que esperamos del usuario.
Pydantic se encarga automáticamente de validar que los datos cumplan con las reglas.

¿Qué es Pydantic?
- Es una librería de Python que valida datos automáticamente
- Define "modelos" que especifican qué tipo de datos esperamos
- Si los datos no cumplen las reglas, lanza errores automáticamente

¿Por qué es importante validar datos?
- Los usuarios pueden enviar datos incorrectos (por error o maliciosamente)
- Sin validación, nuestra aplicación podría fallar o tener problemas de seguridad
- La validación nos ayuda a dar mensajes de error claros al usuario
"""

# ========== IMPORTACIONES ==========
from pydantic import BaseModel, EmailStr, field_validator


# ========== MODELO DE USUARIO ==========
class User(BaseModel):
    """
    🧑‍💻 Modelo de Usuario - Define cómo debe ser un usuario válido
    
    Este modelo especifica:
    - Qué campos debe tener un usuario (email y password)
    - Qué tipo de datos esperamos en cada campo
    - Qué reglas de validación debe cumplir cada campo
    
    BaseModel es la clase base de Pydantic que nos da todas las funcionalidades
    de validación automática.
    """
    
    # 📧 CAMPO EMAIL - Validación automática del formato de email
    # EmailStr es un tipo especial de Pydantic que:
    # - Verifica que el email tenga el formato correcto (usuario@dominio.com)
    # - Se asegura de que contenga @ y un dominio válido
    # - Automáticamente lanza un error si el formato es incorrecto
    email: EmailStr
    
    # 🔐 CAMPO PASSWORD - Campo de texto obligatorio
    # str significa que esperamos una cadena de texto
    # Este campo es obligatorio (si no se proporciona, Pydantic lanza un error)
    password: str
    
    # ========== VALIDACIONES PERSONALIZADAS ==========
    
    # 🛡️ VALIDADOR PERSONALIZADO - Reglas adicionales para la contraseña
    # @field_validator nos permite crear reglas de validación personalizadas
    # En este caso, validamos que la contraseña tenga al menos 8 caracteres
    @field_validator('password')
    @classmethod  # Agregamos @classmethod para mejor práctica
    def validar_longitud_password(cls, valor_password):
        """
        🔍 Valida que la contraseña tenga al menos 8 caracteres
        
        Parámetros:
        - cls: La clase (User) - no lo usamos pero es requerido
        - valor_password: El valor de la contraseña que escribió el usuario
        
        Retorna:
        - El valor de la contraseña si es válido
        
        Lanza:
        - ValueError si la contraseña es muy corta
        """
        # Verificamos la longitud de la contraseña
        if len(valor_password) < 8:
            # Si es muy corta, lanzamos un error con un mensaje claro
            raise ValueError('❌ La contraseña debe tener al menos 8 caracteres.')
        
        # Si la validación pasa, devolvemos el valor (esto es importante)
        return valor_password
    
    # 💡 EJEMPLO DE VALIDACIÓN ADICIONAL (comentado para que veas cómo agregar más)
    # @field_validator('password')
    # @classmethod
    # def validar_password_segura(cls, valor_password):
    #     """Valida que la contraseña tenga al menos una mayúscula y un número"""
    #     if not any(c.isupper() for c in valor_password):
    #         raise ValueError('La contraseña debe tener al menos una mayúscula')
    #     if not any(c.isdigit() for c in valor_password):
    #         raise ValueError('La contraseña debe tener al menos un número')
    #     return valor_password


# ========== CÓMO FUNCIONA TODO ESTO ==========
"""
🔄 FLUJO DE VALIDACIÓN:

1. El usuario llena el formulario y hace clic en "Login"
2. FastAPI recibe los datos del formulario
3. En main.py, intentamos crear un objeto User con esos datos:
   usuario = User(email=email, password=password)
4. Pydantic automáticamente valida:
   - Que el email tenga formato válido (gracias a EmailStr)
   - Que la contraseña tenga al menos 8 caracteres (gracias a nuestro validador)
5. Si todo está bien, se crea el objeto User sin problemas
6. Si algo está mal, Pydantic lanza un ValidationError con detalles del error
7. En main.py capturamos ese error y se lo mostramos al usuario

🎯 BENEFICIOS DE ESTE ENFOQUE:
- Validación automática y consistente
- Mensajes de error claros para el usuario
- Código limpio y fácil de mantener
- Fácil agregar nuevas validaciones
"""