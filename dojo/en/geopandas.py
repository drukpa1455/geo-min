import requests
import geopandas as gpd
from shapely.geometry import Point
import folium
from geopandas.tools import geocode
import pygeos
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import os

# URLs to download GeoJSON and TIFF files
urls = [
    "https://gist.github.com/wavded/1200773/raw/99c1af9980b295bc882ab813a1a0f16536d60236/sample.json",
    "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Tiff-File-download.tiff"
]

# Downloading GeoJSON and TIFF files
for url in urls:
    r = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, 'wb') as file:
        file.write(r.content)

# Load downloaded GeoJSON file
gdf = gpd.read_file('sample.json')

# 1.1 Data Structures: Uniting Geometry and Tabular Data
gs = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
gdf = gpd.GeoDataFrame({'geometry': gs})

# 1.2 Reading and Writing Files: Embracing the Spatial Narratives
gdf = gpd.read_file('sample.json')  # Load GeoJSON file as a GeoDataFrame

# 1.3 Indexing and Selecting Data: A Glimpse of Geometric Wonders
first_geometry = gdf.loc[0, 'geometry']  # Select the geometry of the first row

# 1.4 Making Maps and Plots: Painting the World with Spatial Elegance
gdf.plot()  # Create a plot of the GeoDataFrame

# 1.5 Interactive Mapping: Unleashing Spatial Tales with Interactivity
m = folium.Map([51.5, -0.25], zoom_start=10)  # Create an interactive map
folium.GeoJson(gdf).add_to(m)  # Add GeoJSON data to the map

# 1.6 Projections: Transforming Perspectives, Illuminating the World
gdf = gdf.to_crs(epsg=4326)  # Change the coordinate reference system (CRS) to EPSG 4326

# 1.7 Geometric Manipulations: Sculpting Spatial Beauty
buffered_gdf = gdf.buffer(distance=1)  # Create a buffer around the geometries

# 1.8 Set Operations with Overlay: Uniting and Distinguishing Spatial Tales
gdf1 = gdf.copy()
gdf2 = gdf.copy()
result = gpd.overlay(gdf1, gdf2, how='intersection')  # Perform an intersection between two GeoDataFrames

# 1.9 Aggregation with Dissolve: Blending the Spatial Essence
gdf['category'] = ['cat1', 'cat2', 'cat1']
aggregated = gdf.dissolve(by='category')  # Dissolve geometries based on a column

# 1.10 Merging Data: Fusing Spatial Narratives
gdf1['key'] = ['A', 'B', 'C']
gdf2['key'] = ['B', 'A', 'C']
merged = gdf1.merge(gdf2, on='key')  # Merge two GeoDataFrames based on a common column

# 1.11 Geocoding: Enchanting Addresses into Spatial Coordinates
geocoded = geocode("1600 Pennsylvania Ave NW, Washington, DC 20500", provider='nominatim')  # Convert address to coordinates

# 1.12 Sampling Points: Capturing Spatial Essence with Delicacy
# Assuming that gdf's geometry column contains lines
gdf['geometry'] = pygeos.line_interpolate_point(gdf['geometry'], 0.5)  # Sample points along the lines

# 2.2 Re-projecting using GDAL with Rasterio and Fiona: Harmonizing Spatial Perspectives
with rasterio.open('Sample-Tiff-File-download.tiff') as src:  # Open the TIFF file
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

    with rasterio.open('output.tif', 'w', **kwargs) as dst:  # Create a new TIFF file with reprojected data
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

# 3.2 GeoDataFrame: Fusing Geometry and Tabular Beauty
gdf = gpd.GeoDataFrame({'geometry': gs})  # Create a GeoDataFrame with the GeoSeries
total_area = gdf['geometry'].area.sum()  # Calculate the total area of all geometries

# 3.3 Input/Output: Unveiling the Gateway to Spatial Worlds
gdf.to_file('output.geojson', driver='GeoJSON')  # Save the GeoDataFrame as a GeoJSON file

# 3.4 Tools: Unleashing High-level Spatial Mastery
gdf1 = gpd.read_file('sample.json')  # Load a GeoJSON file as a GeoDataFrame
gdf2 = gpd.read_file('sample.json')  # Load a GeoJSON file as a GeoDataFrame
joined = gpd.sjoin(gdf1, gdf2, how='inner', op='intersects')  # Perform a spatial join between two GeoDataFrames

# Print the loaded GeoDataFrame
print(gdf)