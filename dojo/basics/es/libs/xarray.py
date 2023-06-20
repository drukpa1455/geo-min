import urllib.request
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dask.array as da
import torch

# Visión general
# 1.1 ¿Qué es xarray?
# Xarray es una biblioteca de Python para trabajar con arreglos y conjuntos de datos multidimensionales etiquetados. Proporciona una API poderosa y expresiva que permite la manipulación eficiente de datos, el análisis y la visualización.

# 1.2 ¿Por qué xarray?
# Xarray ofrece varias ventajas, incluyendo:
# - Indexación y selección basada en etiquetas
# - Manejo flexible de datos faltantes
# - Integración perfecta con pandas para datos tabulares
# - Soporte para cómputo paralelo con Dask
# - Extensibilidad para integración con otras bibliotecas

# Paso 1: Descargar el conjunto de datos
url = 'https://www.ncei.noaa.gov/data/climate-indices/ersst.v5.1880-2021.nc'
file_path = 'ersst.v5.1880-2021.nc'
urllib.request.urlretrieve(url, file_path)

# Paso 2: Cargar el conjunto de datos
ds = xr.open_dataset('ersst.v5.1880-2021.nc')

# Estructuras de datos
# Conjunto de datos
# Acceder a variables específicas
sst = ds['sst']
anom = ds['anom']

# Acceder a dimensiones y coordenadas
dims = ds.dims
coords = ds.coords

# DataArray
# Acceder a variables específicas
sst = ds['sst']
anom = ds['anom']

# Acceder a dimensiones y coordenadas
dims = ds.dims
coords = ds.coords

# E/S
# Lectura de datos (ya cubierto en la Guía de inicio rápido)

# Escritura de datos
# Guardar el conjunto de datos en un archivo netCDF
ds.to_netcdf('output.nc')

# Cálculos
# Operaciones
# Realizar cálculos en variables
mean_sst = sst.mean(dim='time')
std_anom = anom.std(dim='time')

# Agregaciones
# Realizar agregaciones en variables
max_sst = sst.max(dim='time')
min_anom = anom.min(dim='time')

# Difusión
# Difundir variables para que coincidan en dimensiones
broadcasted = xr.broadcast(sst, anom)

# Visualización
# Visualización básica
# Graficar la temperatura media de la superficie del mar
mean_sst.plot()

# Agregar título y etiquetas
plt.title('Temperatura Media de la Superficie del Mar')
plt.xlabel('Longitud')
plt.ylabel('Latitud')

# Mostrar la gráfica
plt.show()

# Visualización avanzada (no aplicable en este ejemplo)

# Guía del usuario
# Estructuras de datos (ya cubierto en la Guía de inicio rápido)

# Cálculos
# Valores faltantes / Valores de relleno
# Manejar valores faltantes
masked_sst = xr.where(sst > 0, sst, np.nan)

# Rellenar valores faltantes con interpolación
filled_sst = masked_sst.interpolate_na(dim='time')

# Agrupar: Dividir, Aplicar, Combinar
# Agrupar por una dimensión específica y calcular la media
grouped_mean_sst = sst.groupby('time.month').mean()

# Remuestreo y operaciones agrupadas
# Remuestrear los datos a una frecuencia diferente
resampled_sst = sst.resample(time='Y').mean()

# Operaciones de ventana
# Calcular la media móvil en una ventana de tiempo
rolling_mean_sst = sst.rolling(time=12, center=True).mean()

# Operaciones de ventana móvil (no aplicable en este ejemplo)

# Visualización
# Gráficos 1D
# Gráfico de línea de la temperatura de la superficie del mar
sst.plot.line(x='time')

# Histograma de la temperatura de la superficie del mar
sst.plot.hist()

# Gráficos 2D
# Mapa de calor de la temperatura de la superficie del mar
sst.plot.imshow()

# Gráfico de contorno de la temperatura de la superficie del mar
sst.plot.contour()

# FacetGrid (no aplicable en este ejemplo)

# Indexación y selección de datos
# Selección basada en etiquetas
# Seleccionar datos basados en coordenadas específicas
subset = sst.sel(lat=0, lon=slice(-180, -90))

# Selección basada en posición
# Seleccionar datos basados en índices posicionales
subset = sst.isel(lat=0, lon=slice(0, 100))

# Indexación avanzada
# Seleccionar datos basados en condiciones booleanas
subset = sst.where(sst > 20, drop=True)

# Interpolación
# Interpolación 1D
# Interpolar datos a lo largo de una dimensión
interpolated_sst = sst.interp(time=['2000-01-01', '2000-02-01'])

# Interpolación multidimensional
# Interpolar datos en una nueva cuadrícula
interpolated_grid = sst.interp(lat=[0, 10, 20], lon=[-120, -110, -100])

# Combinación de datos
# Combinar
# Combinar dos conjuntos de datos
ds2 = xr.open_dataset('another_dataset.nc')
merged = xr.merge([ds, ds2])

# Concatenación
# Concatenar dos conjuntos de datos a lo largo de una dimensión
concatenated = xr.concat([ds, ds2], dim='time')

# Comparación
# Comparar dos conjuntos de datos para la igualdad
are_equal = ds.equals(ds2)

# Trabajar con pandas
# Conversión a objetos pandas
# Convertir el conjunto de datos en un DataFrame de pandas
df = ds.to_dataframe()

# Conversión desde objetos pandas
# Convertir un DataFrame de pandas en un conjunto de datos
ds_from_df = xr.Dataset.from_dataframe(df)

# Trabajar con Dask
# Usando arreglos Dask
# Crear un arreglo Dask a partir de un arreglo NumPy
numpy_array = np.random.rand(100, 100)
dask_array = da.from_array(numpy_array, chunks=(10, 10))

# Convertir un arreglo Dask a DataArray de xarray
xr_dataarray = xr.DataArray(dask_array)

# Rendimiento y uso de memoria (no aplicable en este ejemplo)

# Usar xarray con otras bibliotecas
# Interoperabilidad
# Convertir un conjunto de datos de xarray a un tensor PyTorch
torch_tensor = torch.from_numpy(ds['sst'].values)

# Ampliar xarray
# Crear un accesor personalizado de xarray
@xr.register_dataarray_accessor('custom')
class CustomAccessor:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def custom_method(self):
        # Implementa tu lógica personalizada aquí
        pass

# Usar el accesor personalizado en un DataArray de xarray
custom_dataarray = ds['sst'].custom.custom_method()

# Cerrar el conjunto de datos
ds.close()