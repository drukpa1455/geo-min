import math
import os
import io
import datetime
import json

# Referencia de la biblioteca
# Funciones incorporadas
## Funciones matemáticas (módulo math)
resultado_raiz_cuadrada = math.sqrt(16)
print("Raíz cuadrada de 16:", resultado_raiz_cuadrada)

## Funciones y métodos de cadenas de texto
longitud_cadena = len("¡Hola, mundo!")
print("Longitud de la cadena:", longitud_cadena)

## Funciones de archivos y E/S (módulos os, io)
ruta_archivo = "ejemplo.txt"
if os.path.exists(ruta_archivo):
    print("El archivo existe")
else:
    print("El archivo no existe")

with open("ejemplo.txt", "r") as archivo:
    contenido_archivo = archivo.read()
    print("Contenido del archivo:", contenido_archivo)

# Tipos incorporados
## Tipos numéricos (int, float, complex)
num = 42
num_float = float(num)
print("Número de punto flotante:", num_float)

### Operaciones numéricas y funciones incorporadas
valor_absoluto = abs(-10)
print("Valor absoluto:", valor_absoluto)

### Conversiones y formateo de tipos numéricos
valor_hexadecimal = hex(255)
print("Valor hexadecimal:", valor_hexadecimal)

## Tipos de secuencias (listas, tuplas, rangos)
mi_lista = [1, 2, 3]
longitud_lista = len(mi_lista)
print("Longitud de la lista:", longitud_lista)

### Operaciones y métodos de secuencias
mi_tupla = (4, 5, 6)
suma_tupla = sum(mi_tupla)
print("Suma de la tupla:", suma_tupla)

### Técnicas de manipulación de listas y tuplas
mi_lista.append(4)
print("Lista modificada:", mi_lista)

## Tipos de mapeo (diccionarios)
mi_diccionario = {"nombre": "Juan", "edad": 25}
llaves_diccionario = mi_diccionario.keys()
print("Llaves del diccionario:", llaves_diccionario)

### Operaciones y métodos de diccionarios
mi_diccionario["ocupacion"] = "Ingeniero"
print("Diccionario modificado:", mi_diccionario)

### Iteración y comprensión de diccionarios
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)

## Tipos de conjunto (set, frozenset)
mi_conjunto = {1, 2, 3}
longitud_conjunto = len(mi_conjunto)
print("Longitud del conjunto:", longitud_conjunto)

### Operaciones y métodos de conjuntos
mi_conjunto.add(4)
print("Conjunto modificado:", mi_conjunto)

### Álgebra de conjuntos y pruebas de pertenencia
interseccion_conjuntos = {2, 3, 4} & {3, 4, 5}
print("Intersección de conjuntos:", interseccion_conjuntos)

# Módulos de la biblioteca estándar
## Módulo os para interacciones con el sistema operativo
### Manipulación de archivos y directorios
tamaño_archivo = os.path.getsize("ejemplo.txt")
print("Tamaño del archivo:", tamaño_archivo)

### Variables de entorno y manejo de procesos
directorio_trabajo_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_trabajo_actual)

## Módulo datetime para manipulación de fechas y horas
### Objetos y operaciones de fecha y hora
fecha_actual = datetime.date.today()
print("Fecha actual:", fecha_actual)

### Formateo y análisis de cadenas de fecha/hora
cadena_fecha = "2022-01-01"
fecha_parseada = datetime.datetime.strptime(cadena_fecha, "%Y-%m-%d").date()
print("Fecha parseada:", fecha_parseada)

## Módulo json para trabajar con datos JSON
### Serialización y deserialización JSON
persona = {"nombre": "Juan", "edad": 30}
datos_json = json.dumps(persona)
print("Datos JSON:", datos_json)

### Trabajando con estructuras de datos JSON
cadena_json = '{"nombre": "Juan", "edad": 30}'
json_parseado = json.loads(cadena_json)
print("JSON parseado:", json_parseado)
