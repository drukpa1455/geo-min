# Documentación de rioxarray 0.14.0

import os
import wget
import zipfile
import rioxarray
import xarray as xr
import matplotlib.pyplot as plt
from shapely.geometry import box

# Descargando un conjunto de datos de muestra
file_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/HYP_LR.tif.zip"
file_path = "./HYP_LR.tif.zip"
wget.download(file_url, file_path)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall("./")
tif_file = "./HYP_LR.tif"

# Abriendo datos raster con rioxarray
rds = rioxarray.open_rasterio(tif_file)

# 2.3.3. Gestionando la pérdida de información con operaciones xarray
# Algunas operaciones de xarray eliminan atributos, puedes usar assign_attrs para reasignarlos.
mean_rds = rds.mean(dim="x").assign_attrs(rds.attrs)
print(mean_rds)

# 4.4. rioxarray.show_versions
# Para comprobar las versiones de rioxarray y sus dependencias
rioxarray.show_versions()

# Utilizando rioxarray para operaciones geoespaciales - Recorte
# Crea una geometría (en este caso una caja) en el mismo CRS que el conjunto de datos de rioxarray
clipping_box = box(minx=-30, miny=-20, maxx=40, maxy=20)

# Luego usa el método clip en el objeto de conjunto de datos de rioxarray
clipped = rds.rio.clip([clipping_box])

# Graficar el raster recortado
clipped.plot()
plt.show()

# Reproyectando
# Usa el método reproject para cambiar el CRS de los datos raster
reprojected = rds.rio.reproject("EPSG:4326")

# Graficar el raster reproyectado
reprojected.plot()
plt.show()

# Remuestreo
# Remuestrea los datos raster a una resolución más baja
resampled = rds.rio.reproject(rds.rio.crs, resolution=(2, 2))

# Graficar el raster remuestreado
resampled.plot()
plt.show()

# Guardar un raster en el disco
# Guarda los datos raster en un nuevo archivo GeoTIFF
reprojected.rio.to_raster("reprojected.tif")
