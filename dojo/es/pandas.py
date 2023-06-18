import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Descargar el conjunto de datos Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nombres = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'clase']
df = pd.read_csv(url, names=nombres)

# Exploración básica de datos
print(df.head(), df.describe(), df.info(), df.isnull().sum())

# Indexación, selección y herramientas computacionales
print(df['clase'], df.loc[:10, 'ancho_sepalo'], df.corr(), df['clase'].str.upper())

# Agrupación por clase, filtrado y visualización
agrupado = df.groupby('clase').mean()
print(agrupado)
filtrado = df[df['longitud_sepalo'] > 5.0]
print(filtrado)
sns.scatterplot(x="longitud_sepalo", y="ancho_sepalo", hue="clase", data=df)
plt.show()

# Guardando y cargando un DataFrame
filtrado.to_csv('iris_filtrado.csv', index=False)
df_cargado = pd.read_csv('iris_filtrado.csv')
print(df_cargado.head())

# Cambiando las opciones de pandas
pd.set_option('display.max_rows', 10)
print(df)

# Mejorando el rendimiento y manejando duplicados
df['clase'] = df['clase'].astype('category')
print(df.info())
print(df[df.duplicated()])

# Escalando a grandes conjuntos de datos, trabajando con datos categóricos y fechas
df_muestra = df.sample(frac=0.1)
print(df_muestra.head())
df['clase'] = df['clase'].astype('category')
fechas = pd.date_range(start='1/1/2022', periods=len(df))
df['fecha'] = fechas
print(df.head())

# Temas avanzados
df['intervalo'] = pd.cut(df['longitud_sepalo'], 5)
print(df.head())

# Descargar otros conjuntos de datos
conjuntos_datos = {
    'titanic.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
    'iris.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/iris.csv',
}

for nombre_archivo, url in conjuntos_datos.items():
    df = pd.read_csv(url)
    print(f"\nCabeza del conjunto de datos {nombre_archivo}:\n", df.head())

# Reformar, ordenar y crear objetos pandas
df = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
df_fundido = pd.melt(df, id_vars=['A'], value_vars=['B', 'C', 'D', 'E'])
print("\nDataFrame fundido:\n", df_fundido)
df_ordenado = df.sort_values(by='A')
print("\nDataFrame ordenado:\n", df_ordenado.head())
s = pd.Series([1, 2, 3, 4, 5])
print("\nSerie:\n", s)