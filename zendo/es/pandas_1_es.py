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
