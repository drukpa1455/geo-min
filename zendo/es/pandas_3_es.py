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