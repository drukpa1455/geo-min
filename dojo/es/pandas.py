import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['longitud-del-sépalo', 'ancho-del-sépalo', 'longitud-del-pétalo', 'ancho-del-pétalo', 'clase']
df = pd.read_csv(url, names=names)  # Cargar el conjunto de datos de Iris desde la URL en un DataFrame llamado 'df'

print(df.head())  # Mostrar las primeras filas del DataFrame
print(df.shape)   # Mostrar la forma del DataFrame (número de filas, número de columnas)
print(df.columns) # Mostrar los nombres de las columnas del DataFrame
print(df.dtypes)  # Mostrar los tipos de datos de cada columna del DataFrame
print(df.describe())  # Mostrar estadísticas descriptivas del DataFrame

grouped = df.groupby('clase')  # Agrupar el DataFrame por la columna 'clase' y asignar el resultado a 'grouped'
print(grouped.mean())  # Calcular las medias de las columnas numéricas dentro de cada grupo

filtered = df[df['longitud-del-sépalo'] > 5.0]  # Filtrar el DataFrame para obtener solo las filas donde 'longitud-del-sépalo' es mayor a 5.0 y asignar el resultado a 'filtered'
print(filtered)  # Mostrar el DataFrame filtrado

plt.hist(df['longitud-del-sépalo'], bins=10)  # Crear un histograma de la columna 'longitud-del-sépalo' con 10 bins
plt.title('Histograma de la Longitud del Sépalo')  # Establecer el título del gráfico
plt.xlabel('Longitud del Sépalo')  # Etiquetar el eje X
plt.ylabel('Frecuencia')  # Etiquetar el eje Y
plt.show()  # Mostrar el histograma

filtered.to_csv('iris_filtrado.csv', index=False)  # Guardar el DataFrame filtrado en un archivo CSV llamado 'iris_filtrado.csv'

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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

# Descargar los conjuntos de datos necesarios
datasets = {
    'titanic.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
    'iris.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/iris.csv',
    'melting_potatoes.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/melting_potatoes.csv',
    'boston_housing.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/boston_housing.csv',
    'wine_quality.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/wine_quality.csv',
    'nyc_weather.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/nyc_weather.csv',
    'stock_prices.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/stock_prices.csv',
    'sales.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/sales.csv',
}

for filename, url in datasets.items():
    response = requests.get(url)
    with open(filename, 'w') as f:
        f.write(response.text)

# Ejemplo de lectura de un archivo CSV (usando el conjunto de datos Titanic)
df = pd.read_csv('titanic.csv')
print("\nLectura del archivo CSV:")
print(df.head())

# Ejemplo de escritura de un archivo CSV
df.to_csv('output.csv', index=False)
print("\nEscritura del archivo CSV: Escrito exitosamente.")

# Ejemplo de ordenamiento de DataFrame por valores de columna (usando el conjunto de datos Iris)
df = pd.read_csv('iris.csv')
df_ordenado = df.sort_values(by='sepal_length')
print("\nDataFrame ordenado:")
print(df_ordenado.head())

# Ejemplo de remodelación de DataFrame utilizando la función 'melt' (usando el conjunto de datos Melting Potatoes)
df = pd.read_csv('melting_potatoes.csv')
melted_df = pd.melt(df, id_vars=['id'], value_vars=['time_1', 'time_2'], var_name='time_type', value_name='time_value')
print("\nDataFrame fundido:")
print(melted_df.head())

# Ejemplo de creación de una Serie
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("\nSerie:")
print(s)

# Ejemplo de operaciones básicas en una Serie (usando el conjunto de datos Boston Housing)
df = pd.read_csv('boston_housing.csv')
s_sum = df['RM'].sum()
s_mean = df['RM'].mean()
print("\nSuma:", s_sum)
print("Media:", s_mean)

# Ejemplo de creación de un DataFrame (usando el conjunto de datos Wine Quality)
data = pd.read_csv('wine_quality.csv')
df = data[['pH', 'alcohol', 'quality']]
print("\nDataFrame:")
print(df.head())

# Ejemplo de selección de datos de un DataFrame
df_subset = df[['pH', 'quality']]
print("\nSubconjunto del DataFrame:")
print(df_subset.head())

# Ejemplo de uso de arrays y escalares de pandas
array = pd.array([1, 2, 3, 4, 5])
escalar = pd.Series(10)
print("\nArray de pandas:")
print(array)
print("\nEscalar de pandas:")
print(escalar)

# Ejemplo de creación de un objeto de índice
indice = pd.Index(['A', 'B', 'C', 'D'])
print("\nObjeto de índice:")
print(indice)

# Ejemplo de uso de desplazamientos de fechas (usando el conjunto de datos NYC Weather)
df = pd.read_csv('nyc_weather.csv')
fechas = pd.to_datetime(df['date'])
desplazamiento = pd.offsets.Day(1)
nuevas_fechas = fechas + desplazamiento
print("\nNuevas fechas:")
print(nuevas_fechas.head())

# Ejemplo de uso de funciones de ventana (usando el conjunto de datos Stock Price)
df = pd.read_csv('stock_prices.csv')
s = df['price']
suma_rodante = s.rolling(window=2).sum()
print("\nFunciones de ventana:")
print(suma_rodante.head())

# Ejemplo de uso de la operación groupby (usando el conjunto de datos Sales)
df = pd.read_csv('sales.csv')
agrupado = df.groupby('region').sum()
print("\nDatos agrupados:")
print(agrupado.head())

# Ejemplo de remuestreo de datos de series temporales (usando el conjunto de datos Stock Price)
df = pd.read_csv('stock_prices.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df_remuestreado = df.resample('M').mean()
print("\nSeries temporales remuestreadas:")
print(df_remuestreado.head())

# Ejemplo de aplicación de estilos a un DataFrame
styled_df = df.head().style.background_gradient(cmap='cool')
print("\nDataFrame con estilo:")
print(styled_df)

# Ejemplo de trazado de un DataFrame
df.plot(kind='line', x='date', y='price')
plt.title('Precios de acciones a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.show()

# Ejemplo de configuración de opciones
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
print("\nOpciones y configuraciones:")
print(df.head())

# Ejemplo de creación de una función personalizada en pandas
def funcion_personalizada(df):
    # Implementación de la función personalizada
    return df

# Uso de la función personalizada
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
resultado = funcion_personalizada(df)
print(resultado)