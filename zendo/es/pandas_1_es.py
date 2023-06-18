import pandas as pd
import matplotlib.pyplot as plt

# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Descargar y cargar el conjunto de datos de Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nombres = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'clase']
df = pd.read_csv(url, names=nombres)

# Exploración básica de datos
print("Exploración básica de datos:")
print("\nMostrar las primeras 5 filas del DataFrame:")
print(df.head())
print("\nMostrar la forma del DataFrame (filas, columnas):")
print(df.shape)
print("\nMostrar los nombres de las columnas:")
print(df.columns)
print("\nMostrar los tipos de datos de cada columna:")
print(df.dtypes)
print("\nMostrar estadísticas resumidas:")
print(df.describe())

# Ejemplo educativo: Acceso a columnas individuales
print("\nEjemplo educativo: Acceso a columnas individuales:")
sepal_length = df['longitud_sepalo']
print(sepal_length.head())

# Análisis de datos - Agrupar por 'clase' y calcular la media de las otras columnas
print("\nAnálisis de datos:")
agrupado = df.groupby('clase')
print("Agrupado por 'clase' y calcular la media de las otras columnas:")
print(agrupado.mean())

# Filtrar filas basadas en una condición - Filtrar filas donde 'longitud_sepalo' sea mayor que 5.0
print("\nFiltrar filas basadas en una condición:")
filtrado = df[df['longitud_sepalo'] > 5.0]
print("Filas filtradas donde 'longitud_sepalo' es mayor que 5.0:")
print(filtrado)

# Crear un histograma para 'longitud_sepalo'
print("\nCrear un histograma para 'longitud_sepalo':")
plt.hist(df['longitud_sepalo'], bins=10)
plt.title('Histograma de la Longitud del Sépalo')
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Frecuencia')
plt.show()

# Ejemplo educativo: Gráfico de dispersión de longitud del sépalo vs. ancho del sépalo
print("\nEjemplo educativo: Gráfico de dispersión de longitud del sépalo vs. ancho del sépalo:")
plt.scatter(df['longitud_sepalo'], df['ancho_sepalo'], c='red')
plt.title('Dispersión de Longitud del Sépalo vs. Ancho del Sépalo')
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.show()

# Ejemplo educativo: Gráfico de barras de la distribución de clases
print("\nEjemplo educativo: Gráfico de barras de la distribución de clases:")
class_counts = df['clase'].value_counts()
plt.bar(class_counts.index, class_counts.values)
plt.title('Distribución de Clases')
plt.xlabel('Clase')
plt.ylabel('Frecuencia')
plt.show()

# Ejemplo educativo: Gráfico de caja de las longitudes de los pétalos por clase
print("\nEjemplo educativo: Gráfico de caja de las longitudes de los pétalos por clase:")
plt.boxplot([df[df['clase'] == 'Iris-setosa']['longitud_petalo'],
             df[df['clase'] == 'Iris-versicolor']['longitud_petalo'],
             df[df['clase'] == 'Iris-virginica']['longitud_petalo']],
            labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
plt.title('Longitudes de los Pétalos por Clase')
plt.xlabel('Clase')
plt.ylabel('Longitud del Pétalo')
plt.show()

# Guardar el DataFrame filtrado en un archivo CSV
print("\nGuardar el DataFrame filtrado en un archivo CSV:")
filtrado.to_csv('iris_filtrado.csv', index=False)
