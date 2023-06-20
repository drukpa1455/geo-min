import requests
import geopandas as gpd
from shapely.geometry import Point
import folium
from geopandas.tools import geocode
import pygeos
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import os

# URLs para descargar archivos GeoJSON y TIFF
urls = [
    "https://gist.github.com/wavded/1200773/raw/99c1af9980b295bc882ab813a1a0f16536d60236/sample.json",
    "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Tiff-File-download.tiff"
]

# Descargar archivos GeoJSON y TIFF
for url in urls:
    r = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, 'wb') as file:
        file.write(r.content)

# Cargar archivo GeoJSON descargado
gdf = gpd.read_file('sample.json')

# 1.1 Estructuras de datos: Unir geometría y datos tabulares
gs = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
gdf = gpd.GeoDataFrame({'geometry': gs})

# 1.2 Lectura y escritura de archivos: Asumiendo narrativas espaciales
gdf = gpd.read_file('sample.json')  # Cargar archivo GeoJSON como GeoDataFrame

# 1.3 Indexación y selección de datos: Un vistazo a maravillas geométricas
first_geometry = gdf.loc[0, 'geometry']  # Seleccionar la geometría de la primera fila

# 1.4 Creación de mapas y gráficos: Pintando el mundo con elegancia espacial
gdf.plot()  # Crear un gráfico del GeoDataFrame

# 1.5 Mapas interactivos: Desatando historias espaciales con interactividad
m = folium.Map([51.5, -0.25], zoom_start=10)  # Crear un mapa interactivo
folium.GeoJson(gdf).add_to(m)  # Agregar datos GeoJSON al mapa

# 1.6 Proyecciones: Transformando perspectivas, iluminando el mundo
gdf = gdf.to_crs(epsg=4326)  # Cambiar el sistema de referencia de coordenadas (CRS) a EPSG 4326

# 1.7 Manipulación geométrica: Moldeando la belleza espacial
buffered_gdf = gdf.buffer(distance=1)  # Crear un búfer alrededor de las geometrías

# 1.8 Operaciones de conjunto con superposición: Uniendo y distinguiendo historias espaciales
gdf1 = gdf.copy()
gdf2 = gdf.copy()
result = gpd.overlay(gdf1, gdf2, how='intersection')  # Realizar una intersección entre dos GeoDataFrames

# 1.9 Agregación con disolución: Mezclando la esencia espacial
gdf['category'] = ['cat1', 'cat2', 'cat1']
aggregated = gdf.dissolve(by='category')  # Disolver geometrías basado en una columna

# 1.10 Fusión de datos: Fusionando narrativas espaciales
gdf1['key'] = ['A', 'B', 'C']
gdf2['key'] = ['B', 'A', 'C']
merged = gdf1.merge(gdf2, on='key')  # Fusionar dos GeoDataFrames basado en una columna común

# 1.11 Geocodificación: Encantando direcciones en coordenadas espaciales
geocoded = geocode("1600 Pennsylvania Ave NW, Washington, DC 20500", provider='nominatim')  # Convertir dirección a coordenadas

# 1.12 Muestreo de puntos: Capturando la esencia espacial con delicadeza
# Suponiendo que la columna de geometría de gdf contiene líneas
gdf['geometry'] = pygeos.line_interpolate_point(gdf['geometry'], 0.5)  # Muestrear puntos a lo largo de las líneas

# 2.2 Reproyección usando GDAL con Rasterio y Fiona: Armonizando perspectivas espaciales
with rasterio.open('Sample-Tiff-File-download.tiff') as src:  # Abrir el archivo TIFF
    transform, width, height = calculate_default_transform(
        src.crs, 'EPSG:4326', src.width, src.height, *src.bounds
    )
    kwargs = src.meta.copy()
    kwargs.update(
        {
            'crs': 'EPSG:4326',
            'transform': transform,
            'width': width,
            'height': height
        }
    )

    with rasterio.open('output.tif', 'w', **kwargs) as dst:  # Crear un nuevo archivo TIFF con los datos reproyectados
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs='EPSG:4326',
                resampling=Resampling.nearest
            )

# 3.2 GeoDataFrame: Fusionando geometría y belleza tabular
gdf = gpd.GeoDataFrame({'geometry': gs})  # Crear un GeoDataFrame con el GeoSeries
total_area = gdf['geometry'].area.sum()  # Calcular el área total de todas las geometrías

# 3.3 Entrada/Salida: Desvelando la puerta de entrada a los mundos espaciales
gdf.to_file('output.geojson', driver='GeoJSON')  # Guardar el GeoDataFrame como un archivo GeoJSON

# 3.4 Herramientas: Desatando el dominio espacial de alto nivel
gdf1 = gpd.read_file('sample.json')  # Cargar un archivo GeoJSON como GeoDataFrame
gdf2 = gpd.read_file('sample.json')  # Cargar un archivo GeoJSON como GeoDataFrame
joined = gpd.sjoin(gdf1, gdf2, how='inner', op='intersects')  # Realizar una unión espacial entre dos GeoDataFrames

# Imprimir el GeoDataFrame cargado
print(gdf)
