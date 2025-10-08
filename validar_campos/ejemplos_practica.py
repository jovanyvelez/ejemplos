"""
🎓 EJEMPLOS PRÁCTICOS PARA ESTUDIANTES
=====================================

Este archivo contiene ejercicios y ejemplos adicionales para que los estudiantes
practiquen y experimenten con Pydantic y validación de datos.

¡Ejecuta este archivo para ver cómo funcionan las validaciones!
"""

from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import Optional, Literal, List
from datetime import date


# ========== EJEMPLO 1: MODELO BÁSICO ==========
print("🔍 EJEMPLO 1: Validación básica")
print("=" * 50)

class Estudiante(BaseModel):
    """Modelo simple de estudiante"""
    nombre: str
    edad: int
    email: EmailStr

# ✅ Caso exitoso
try:
    estudiante = Estudiante(
        nombre="Ana García",
        edad=16,
        email="ana@colegio.edu"
    )
    print(f"✅ Estudiante válido: {estudiante.nombre}, {estudiante.edad} años")
except ValidationError as e:
    print(f"❌ Error: {e}")

# ❌ Caso con error
try:
    estudiante_malo = Estudiante(
        nombre="Juan",
        edad="dieciséis",  # ❌ Debe ser número, no texto
        email="juan@colegio.edu"
    )
except ValidationError as e:
    print(f"❌ Error detectado: {e.errors()[0]['msg']}")

print("\n")


# ========== EJEMPLO 2: VALIDACIONES PERSONALIZADAS ==========
print("🛡️ EJEMPLO 2: Validaciones personalizadas")
print("=" * 50)

class Usuario(BaseModel):
    """Usuario con validaciones más complejas"""
    nombre: str
    edad: int
    email: EmailStr
    telefono: Optional[str] = None
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v):
        """El nombre debe tener al menos 2 caracteres"""
        if len(v.strip()) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        return v.strip().title()  # Capitaliza el nombre
    
    @field_validator('edad')
    @classmethod
    def validar_edad(cls, v):
        """La edad debe estar entre 13 y 100 años"""
        if v < 13:
            raise ValueError('Debes tener al menos 13 años')
        if v > 100:
            raise ValueError('La edad no puede ser mayor a 100 años')
        return v
    
    @field_validator('telefono')
    @classmethod
    def validar_telefono(cls, v):
        """Teléfono debe tener formato básico"""
        if v is None:
            return v
        # Remover espacios y guiones
        telefono_limpio = v.replace(' ', '').replace('-', '')
        if not telefono_limpio.isdigit() or len(telefono_limpio) < 8:
            raise ValueError('Teléfono debe tener al menos 8 dígitos')
        return telefono_limpio

# Pruebas
casos_prueba = [
    {"nombre": "maria", "edad": 15, "email": "maria@test.com"},  # ✅ Válido
    {"nombre": "A", "edad": 20, "email": "a@test.com"},         # ❌ Nombre muy corto
    {"nombre": "Pedro", "edad": 12, "email": "pedro@test.com"}, # ❌ Muy joven
    {"nombre": "Juan", "edad": 25, "email": "juan@test.com", "telefono": "12345678"}, # ✅ Válido
]

for i, datos in enumerate(casos_prueba, 1):
    try:
        usuario = Usuario(**datos)
        print(f"✅ Caso {i}: Usuario válido - {usuario.nombre}")
    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        print(f"❌ Caso {i}: Error - {error_msg}")

print("\n")


# ========== EJEMPLO 3: MODELOS COMPLEJOS ==========
print("🏗️ EJEMPLO 3: Modelos más complejos")
print("=" * 50)

class Direccion(BaseModel):
    """Modelo para direcciones"""
    calle: str
    numero: int
    ciudad: str
    codigo_postal: str
    
    @field_validator('codigo_postal')
    @classmethod
    def validar_codigo_postal(cls, v):
        """Código postal debe tener 5 dígitos"""
        if not v.isdigit() or len(v) != 5:
            raise ValueError('Código postal debe tener exactamente 5 dígitos')
        return v

class EstudianteCompleto(BaseModel):
    """Estudiante con información más completa"""
    nombre: str
    apellido: str
    edad: int
    email: EmailStr
    direccion: Direccion  # ¡Modelo anidado!
    curso: Literal["primero", "segundo", "tercero", "cuarto"]  # Solo valores específicos
    fecha_inscripcion: date
    
    @field_validator('fecha_inscripcion')
    @classmethod
    def validar_fecha_inscripcion(cls, v):
        """No puede ser una fecha futura"""
        if v > date.today():
            raise ValueError('La fecha de inscripción no puede ser en el futuro')
        return v

# Ejemplo de uso
try:
    estudiante_completo = EstudianteCompleto(
        nombre="Carlos",
        apellido="López",
        edad=17,
        email="carlos@colegio.edu",
        direccion=Direccion(
            calle="Av. Principal",
            numero=123,
            ciudad="Madrid",
            codigo_postal="28001"
        ),
        curso="tercero",
        fecha_inscripcion=date(2024, 1, 15)
    )
    print(f"✅ Estudiante completo creado: {estudiante_completo.nombre} {estudiante_completo.apellido}")
    print(f"   Dirección: {estudiante_completo.direccion.calle} {estudiante_completo.direccion.numero}")
except ValidationError as e:
    print(f"❌ Error: {e}")

print("\n")


# ========== EJEMPLO 4: VALIDACIÓN DE LISTAS ==========
print("📋 EJEMPLO 4: Validación de listas")
print("=" * 50)

class Materia(BaseModel):
    """Modelo para materias"""
    nombre: str
    creditos: int
    
    @field_validator('creditos')
    @classmethod
    def validar_creditos(cls, v):
        if v <= 0 or v > 10:
            raise ValueError('Los créditos deben estar entre 1 y 10')
        return v

class EstudianteConMaterias(BaseModel):
    """Estudiante con lista de materias"""
    nombre: str
    email: EmailStr
    materias: List[Materia]  # Lista de objetos Materia
    
    @field_validator('materias')
    @classmethod
    def validar_materias(cls, v):
        if len(v) == 0:
            raise ValueError('El estudiante debe tener al menos una materia')
        if len(v) > 8:
            raise ValueError('El estudiante no puede tener más de 8 materias')
        return v

# Ejemplo con lista de materias
try:
    estudiante_con_materias = EstudianteConMaterias(
        nombre="Laura Fernández",
        email="laura@colegio.edu",
        materias=[
            Materia(nombre="Matemáticas", creditos=5),
            Materia(nombre="Historia", creditos=3),
            Materia(nombre="Inglés", creditos=4)
        ]
    )
    print(f"✅ Estudiante con materias: {estudiante_con_materias.nombre}")
    print(f"   Materias: {[m.nombre for m in estudiante_con_materias.materias]}")
except ValidationError as e:
    print(f"❌ Error: {e}")

print("\n")


# ========== EJERCICIOS PARA ESTUDIANTES ==========
print("🎯 EJERCICIOS PARA PRACTICAR")
print("=" * 50)
print("""
¡Ahora es tu turno! Intenta crear los siguientes modelos:

1. 📚 LIBRO
   - título (obligatorio, mínimo 3 caracteres)
   - autor (obligatorio)
   - año_publicacion (entre 1000 y 2024)
   - isbn (exactamente 13 dígitos)
   - precio (mayor a 0)

2. 🏫 COLEGIO
   - nombre (obligatorio)
   - direccion (usar el modelo Direccion)
   - estudiantes (lista de estudiantes, máximo 1000)
   - año_fundacion (no puede ser futuro)

3. 📝 EXAMEN
   - materia (texto obligatorio)
   - fecha (no puede ser pasada)
   - duracion_minutos (entre 30 y 240 minutos)
   - nota_maxima (entre 1 y 100)

4. 🎓 PROFESOR
   - nombre y apellido (obligatorios)
   - materias_que_enseña (lista de strings, mínimo 1)
   - años_experiencia (mayor o igual a 0)
   - salario (opcional, pero si se proporciona debe ser mayor a 0)

¡Prueba diferentes casos de error para ver cómo funcionan las validaciones!
""")


# ========== FUNCIÓN DE DEMOSTRACIÓN ==========
def demostrar_validacion():
    """
    Función para demostrar validaciones paso a paso
    """
    print("🔍 DEMOSTRACIÓN INTERACTIVA")
    print("=" * 50)
    
    class EjemploInteractivo(BaseModel):
        edad: int
        
        @field_validator('edad')
        @classmethod
        def validar_edad(cls, v):
            print(f"   🔍 Validando edad: {v}")
            if v < 0:
                print("   ❌ Edad no puede ser negativa")
                raise ValueError("La edad no puede ser negativa")
            if v > 150:
                print("   ❌ Edad demasiado alta")
                raise ValueError("La edad no puede ser mayor a 150")
            print("   ✅ Edad válida")
            return v
    
    # Casos de prueba con explicación paso a paso
    casos = [25, -5, 200, 16]
    
    for edad in casos:
        print(f"\n🧪 Probando edad: {edad}")
        try:
            ejemplo = EjemploInteractivo(edad=edad)
            print(f"   🎉 Resultado: Objeto creado exitosamente")
        except ValidationError as e:
            print(f"   💥 Error capturado: {e.errors()[0]['msg']}")

# Ejecutar demostración
demostrar_validacion()


if __name__ == "__main__":
    print("\n🎓 ¡Has terminado de revisar todos los ejemplos!")
    print("💡 Ahora prueba a modificar este código y experimentar con tus propias validaciones.")
    print("🚀 ¡La práctica hace al maestro!")