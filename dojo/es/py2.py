# Comenzando
print("Hola, Mundo!")

# Comprendiendo la sintaxis y estructura de Python
# Flujo básico de ejecución del programa
# Interactuando con la consola de Python

# Sintaxis básica
# Variables y asignaciones
mi_variable = 10
print(mi_variable)

# Convenciones de nombres y mejores prácticas
# Tipos de variables y tipado dinámico
# Alcance y duración de las variables

# Operadores y expresiones
a = 5
b = 3
suma = a + b
print(suma)

# Operadores aritméticos
# Operadores de comparación y lógicos
# Precedencia y asociatividad de operadores

# Estructuras condicionales (if-else)
x = 10
if x > 0:
    print("Positivo")
else:
    print("No positivo")

# Sintaxis y uso
# Múltiples condiciones (if-elif-else)
# Expresiones condicionales (operador ternario)

# Variables y Tipos de Datos
# Números
x = 5
y = 2.5
z = complex(1, 2)
print(x, y, z)

# Enteros, flotantes y números complejos
# Operaciones y conversiones numéricas

# Cadenas de texto y manipulación de cadenas
mensaje = "Hola, Python!"
print(mensaje)

# Literales de cadena y secuencias de escape
# Métodos de cadena y formato
# Expresiones regulares (módulo re)

# Listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Creación y acceso a listas
# Métodos de lista y segmentación
# Comprensión de listas

# Tuplas
coordenadas = (3, 4)
print(coordenadas)

# Creación y acceso a tuplas
# Empaquetado y desempaquetado de tuplas
# Naturaleza inmutable y casos de uso

# Diccionarios
persona = {"nombre": "Juan", "edad": 30}
print(persona)

# Creación y acceso a diccionarios
# Métodos y operaciones de diccionarios
# Comprensión de diccionarios

# Conjuntos
frutas = {"manzana", "banana", "cereza"}
print(frutas)

# Creación y manipulación de conjuntos
# Operaciones de conjuntos (unión, intersección, etc.)
# Comprensión de conjuntos

# Control de flujo
# Bucles (for y while)
for i in range(5):
    print(i)

# Iteración sobre secuencias y rangos
# Sentencias de control de bucles (break y continue)
# Bucles anidados y constructo loop-else

# Estructuras condicionales (if-elif-else)
x = 5
if x > 0:
    print("Positivo")
elif x < 0:
    print("Negativo")
else:
    print("Cero")

# Combinación de condiciones con operadores lógicos
# Comparaciones encadenadas y evaluación perezosa
# Expresiones condicionales y operador "in"

# Funciones
def saludar(nombre):
    print("Hola, " + nombre + "!")

saludar("Alice")

# Definición de funciones
# Sintaxis y estructura de funciones
# Argumentos de funciones (posicionales, por palabra clave, por defecto)
# Argumentos de longitud variable (*args, **kwargs)

# Alcance de funciones y espacios de nombres
# Variables globales y locales
# Enmascaramiento de variables

# Valores de retorno y None
# Devolución de valores desde funciones
# El objeto None y su significado

# Documentación de funciones y docstrings
# Escribir documentación significativa de funciones
# Uso y acceso a docstrings

# Módulos y Paquetes
import math

# Creación e importación de módulos
# Conceptos de programación modular
# Estructura y organización de módulos
# Importación de módulos y espacios de nombres

# Estructura de paquetes e importación
# Empaquetar código Python en módulos y subpaquetes
# Configuración de directorios y archivos de paquetes
# Importación desde paquetes y subpaquetes

# Entrada/Salida de archivos
# Lectura y escritura de archivos de texto
archivo = open("ejemplo.txt", "w")
archivo.write("¡Hola, Archivo!")
archivo.close()

# Apertura y cierre de archivos
# Métodos de lectura (read, readline, readlines)
# Métodos de escritura (write, writelines)

# Trabajo con objetos de archivo
# Modos de archivo y permisos de acceso
# Posición y búsqueda en el archivo
# Mejores prácticas de manejo de archivos (sentencia with)

# Manejo de Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# Manejo de excepciones específicas
# Captura y manejo de tipos de error específicos
# Múltiples cláusulas except y jerarquía de excepciones

# Uso de bloques try-except
# Sintaxis y estructura de try-except
# Manejo de múltiples excepciones
# Manejo y registro de excepciones

# La cláusula finally
# Ejecución de código independientemente de la ocurrencia de excepciones
# Casos de uso de finally (liberación de recursos)

# Programación Orientada a Objetos
# Clases y objetos
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

circulo = Circulo(5)
print(circulo.area())

# Definición de clases e instanciación de objetos
# Atributos de clase y atributos de instancia
# El parámetro self y métodos de instancia

# Herencia y polimorfismo
# Creación de clases derivadas y redefinición de métodos
# Orden de resolución de métodos (MRO)
# Polimorfismo y duck typing

# Encapsulación y abstracción
# Modificadores de acceso (público, privado, protegido)
# Métodos getter y setter
# Clases abstractas e interfaces

# Expresiones Regulares
import re

patron = r"\d+"
coincidencias = re.findall(patron, "Tengo 2 manzanas y 3 naranjas")
print(coincidencias)

# Coincidencia de patrones con el módulo re
# Sintaxis y patrones de expresiones regulares
# Operaciones de coincidencia y búsqueda
# Agrupación y captura

# Modificadores de expresiones regulares
# Modos de coincidencia (insensible a mayúsculas y minúsculas, multilinea, etc.)
# Anclas y delimitadores de límites
# Asertos de vista previa y de retroceso

# Depuración
x = 5
print("Antes del punto de interrupción")
# Inserta un punto de interrupción aquí
print("Después del punto de interrupción")
