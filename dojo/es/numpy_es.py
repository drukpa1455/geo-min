import numpy as np
from sklearn.datasets import load_iris

# Introducción a NumPy
# NumPy es una librería de Python para la computación numérica. Proporciona soporte para grandes arreglos y matrices multidimensionales, junto con una colección de funciones matemáticas para operar en estos arreglos de manera eficiente.

# Arreglos
# Un arreglo es una estructura de datos central en NumPy. Es una cuadrícula de valores, todos del mismo tipo, e indexada por una tupla de enteros no negativos.

# Creando Arreglos
mi_lista = [1, 2, 3, 4, 5]
mi_arreglo = np.array(mi_lista)  # Convertir una lista a un arreglo de NumPy
print(mi_arreglo)
# Salida: [1 2 3 4 5]

arreglo_ceros = np.zeros((3, 4))  # Crear un arreglo de 3x4 lleno de ceros
arreglo_unos = np.ones((2, 2))  # Crear un arreglo de 2x2 lleno de unos
arreglo_random = np.random.random((2, 3))  # Crear un arreglo de 2x3 con números aleatorios entre 0 y 1

print(arreglo_ceros)
print(arreglo_unos)
print(arreglo_random)

# Atributos de los Arreglos
mi_arreglo = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_arreglo.shape)  # Forma del arreglo
# Salida: (2, 3)
print(mi_arreglo.dtype)  # Tipo de datos del arreglo
# Salida: int64
print(mi_arreglo.size)  # Número de elementos en el arreglo
# Salida: 6
print(mi_arreglo.ndim)  # Número de dimensiones del arreglo
# Salida: 2

# Indexación de Arreglos
mi_arreglo = np.array([1, 2, 3, 4, 5])
print(mi_arreglo[0])  # Acceder al primer elemento
# Salida: 1
print(mi_arreglo[3])  # Acceder al cuarto elemento
# Salida: 4

mi_arreglo = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_arreglo[0, 1])  # Acceder al elemento en la fila 0, columna 1
# Salida: 2
print(mi_arreglo[1, 2])  # Acceder al elemento en la fila 1, columna 2
# Salida: 6

# Cortar Arreglos
mi_arreglo = np.array([1, 2, 3, 4, 5])
print(mi_arreglo[1:4])  # Cortar los elementos desde el índice 1 al 3
# Salida: [2 3 4]
print(mi_arreglo[:3])  # Cortar los elementos desde el inicio hasta el índice 2
# Salida: [1 2 3]
print(mi_arreglo[::2])  # Cortar los elementos con un paso de tamaño 2
# Salida: [1 3 5]

mi_arreglo = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_arreglo[:, 1:])  # Cortar todas las filas y columnas a partir del índice 1
# Salida: [[2 3]
#          [5 6]]

# Cambio de forma de los Arreglos
mi_arreglo = np.array([1, 2, 3, 4, 5, 6])
arreglo_redimensionado = mi_arreglo.reshape((2, 3))  # Cambiar la forma del arreglo a una matriz de 2x3

print(arreglo_redimensionado)
# Salida: [[1 2 3]
#          [4 5 6]]

# Operaciones con Arreglos
arreglo1 = np.array([1, 2, 3])
arreglo2 = np.array([4, 5, 6])

resultado = arreglo1 + arreglo2
print(resultado)
# Salida: [5 7 9]

resultado = arreglo1 * arreglo2
print(resultado)
# Salida: [4 10 18]

resultado = np.maximum(arreglo1, arreglo2)
print(resultado)
# Salida: [4 5 6]

# Funciones Matemáticas
arreglo = np.array([0, np.pi/2, np.pi])
resultado = np.sin(arreglo)
print(resultado)
# Salida: [0.00000000e+00 1.00000000e+00 1.22464680e-16]

arreglo = np.array([1, 10, 100])
resultado = np.log10(arreglo)
print(resultado)
# Salida: [0. 1. 2.]

arreglo = np.array([0, 1, 2])
resultado = np.exp(arreglo)
print(resultado)
# Salida: [1.         2.71828183 7.3890561 ]

# Álgebra Lineal
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.matmul(matriz1, matriz2)
print(resultado)
# Salida: [[19 22]
#          [43 50]]

matriz = np.array([[1, 2], [3, 4]])
matriz_inversa = np.linalg.inv(matriz)
print(matriz_inversa)
# Salida: [[-2.   1. ]
#          [ 1.5 -0.5]]

# Generación de Números Aleatorios
entero_aleatorio = np.random.randint(10)
print(entero_aleatorio)

muestras_aleatorias = np.random.normal(size=(3, 3))
print(muestras_aleatorias)

# Entrada y Salida
arreglo = np.array([1, 2, 3, 4, 5])
np.save('mi_arreglo.npy', arreglo)

arreglo_cargado = np.load('mi_arreglo.npy')
print(arreglo_cargado)
# Salida: [1 2 3 4 5]

# Broadcasting
arreglo1 = np.array([1, 2, 3])
escalar = 2
resultado = arreglo1 * escalar
print(resultado)
# Salida: [2 4 6]

# Temas Avanzados

# Funciones Vectorizadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

sigmoid_vectorizada = np.vectorize(sigmoid)
arreglo = np.array([0, 1, 2, 3])
resultado = sigmoid_vectorizada(arreglo)
print(resultado)
# Salida: [0.5        0.73105858 0.88079708 0.95257413]

# Optimización de Memoria
gran_arreglo = np.ones((1000, 1000))
print(gran_arreglo.nbytes)
# Salida: 8000000 (8 megabytes)

# Arreglos Estructurados
arreglo_estructurado = np.array([(1, 2.0, 'Hola'), (2, 3.5, 'Mundo')],
                            dtype=[('entero', int), ('flotante', float), ('cadena', object)])
print(arreglo_estructurado['entero'])
# Salida: [1 2]
print(arreglo_estructurado['flotante'])
# Salida: [2.  3.5]
print(arreglo_estructurado['cadena'])
# Salida: ['Hola' 'Mundo']

# Indexación Elegante
arreglo = np.array([1, 2, 3, 4, 5])
mascara = arreglo > 2
print(arreglo[mascara])
# Salida: [3 4 5]

# Funciones Universales
arreglo = np.array([1, 2, 3, 4, 5])
resultado = np.square(arreglo)
print(resultado)
# Salida: [ 1  4  9 16 25]

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Variable objetivo

# Realizar operaciones usando el conjunto de datos Iris
# Ejemplo: Calcular la media de las longitudes de los sépalos utilizando la primera característica (longitud del sépalo)
media_longitud_sepalo = np.mean(X[:, 0])
print(media_longitud_sepalo)

# Ejemplo: Seleccionar las primeras tres filas del conjunto de datos
subconjunto = X[:3, :]
print(subconjunto)

# Ejemplo: Calcular la suma de cada columna en el conjunto de datos
sumas_columnas = np.sum(X, axis=0)
print(sumas_columnas)

# Ejemplo: Calcular el producto escalar de dos columnas de características
producto_punto = np.dot(X[:, 0], X[:, 1])
print(producto_punto)

# ... (Más temas avanzados)

# Puede encontrar información y ejemplos más detallados en la documentación oficial de NumPy.
