# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos iris
iris = sns.load_dataset('iris')

# Mostrar las primeras cinco filas del conjunto de datos
print("\nConjunto de datos Iris cargado:")
print(iris.head())

# --------------- FUNCIONALIDAD BÁSICA ESENCIAL ---------------
# El método 'describe' proporciona estadísticas básicas para cada columna del conjunto de datos.
print("\nEstadísticas descriptivas del conjunto de datos Iris:")
print(iris.describe())

# El método 'info' muestra información sobre un DataFrame, incluyendo el tipo de índice, columnas, valores no nulos y uso de memoria.
print("\nInformación sobre el conjunto de datos Iris:")
print(iris.info())

# --------------- INDEXACIÓN Y SELECCIÓN DE DATOS ---------------
# Seleccionar una columna específica del conjunto de datos iris
print("\nSeleccionar la columna 'species' del conjunto de datos Iris:")
print(iris['species'])

# Seleccionar las primeras 10 filas de una columna específica utilizando indexación basada en etiquetas
print("\nPrimeras 10 filas de la columna 'petal_width':")
print(iris.loc[:10, 'petal_width'])

# --------------- HERRAMIENTAS COMPUTACIONALES ---------------
# El método 'corr' calcula la matriz de correlación para el conjunto de datos iris
print("\nMatriz de correlación del conjunto de datos Iris:")
print(iris.corr())

# --------------- TRABAJO CON DATOS DE TEXTO ---------------
# El método 'str.upper' convierte los nombres de las especies a mayúsculas
print("\nColumna 'species' en mayúsculas:")
print(iris['species'].str.upper())

# --------------- TRABAJO CON DATOS FALTANTES ---------------
# El método 'isnull().sum()' devuelve la cantidad de valores faltantes en cada columna
print("\nCantidad de valores faltantes en cada columna:")
print(iris.isnull().sum())

# --------------- AGRUPACIÓN DE DATOS ---------------
# El método 'groupby' agrupa los datos por especie y calcula la media para cada grupo
print("\nMedia de todas las columnas numéricas, agrupadas por especie:")
print(iris.groupby('species').mean())

# --------------- VISUALIZACIÓN ---------------
# Graficar un gráfico de barras de la longitud promedio del pétalo para cada especie
print("\nGráfico de barras de la longitud promedio del pétalo para cada especie:")
iris.groupby('species')['petal_length'].mean().plot(kind='bar')
plt.show()

# Graficar histogramas para cada característica del conjunto de datos
iris.hist(edgecolor='black', linewidth=1.2)
plt.show()

# Graficar un gráfico de dispersión con codificación de color por especie
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.show()

# --------------- OPCIONES Y CONFIGURACIONES ---------------
# El método 'set_option' cambia la cantidad máxima de filas mostradas
pd.set_option('display.max_rows', 10)
print("\nNueva configuración de cantidad máxima de filas mostradas:")
print(iris)

# --------------- MEJORA DEL RENDIMIENTO ---------------
# Cambiar el tipo de datos de la columna 'species' a 'category' para ahorrar memoria
iris['species'] = iris['species'].astype('category')
print("\nConjunto de datos Iris con la columna 'species' como tipo de categoría:")
print(iris.info())

# --------------- ESCALADO A CONJUNTOS DE DATOS GRANDES ---------------
# El método 'sample' extrae una muestra aleatoria (10%) del DataFrame
iris_muestra = iris.sample(frac=0.1)
print("\nConjunto de datos Iris muestreado:")
print(iris_muestra.head())

# --------------- MANEJO DE ETIQUETAS DUPLICADAS ---------------
# El método 'duplicated()' imprime las filas duplicadas en el conjunto de datos iris
print("\nFilas duplicadas en el conjunto de datos Iris:")
print(iris[iris.duplicated()])

# --------------- TRABAJO CON DATOS CATEGÓRICOS ---------------
# Cambiar 'species' a un tipo de dato categórico
iris['species'] = iris['species'].astype('category')
print("\nColumna 'species' como tipo de dato categórico:")
print(iris['species'])

# --------------- TRABAJO CON FECHAS Y SERIES TEMPORALES ---------------
# Crear un rango de fechas simple (una para cada fila del conjunto de datos iris)
fechas = pd.date_range(start='1/1/2022', periods=len(iris))
iris['fecha'] = fechas
print("\nConjunto de datos Iris con columna de fechas:")
print(iris.head())

# --------------- TEMAS AVANZADOS ---------------
# Crear un índice de intervalo
df = pd.DataFrame({'A': range(5)})
df.index = pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4, 5])
print("\nDataFrame con índice de intervalo:")
print(df)
