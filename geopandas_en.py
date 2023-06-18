import geopandas as gpd
from shapely.geometry import Point
import folium
from geopandas.tools import geocode
import pygeos
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

# GeoPandas guide

# 1. User Guide: Unveiling the Core

# 1.1 Data Structures: Uniting Geometry and Tabular Data
gs = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
gdf = gpd.GeoDataFrame({'geometry': gs})

# 1.2 Reading and Writing Files: Embracing the Spatial Narratives
gdf = gpd.read_file('example.geojson')

# 1.3 Indexing and Selecting Data: A Glimpse of Geometric Wonders
first_geometry = gdf.loc[0, 'geometry']

# 1.4 Making Maps and Plots: Painting the World with Spatial Elegance
gdf.plot()

# 1.5 Interactive Mapping: Unleashing Spatial Tales with Interactivity
m = folium.Map([51.5, -0.25], zoom_start=10)
folium.GeoJson(gdf).add_to(m)

# 1.6 Projections: Transforming Perspectives, Illuminating the World
gdf = gdf.to_crs(epsg=4326)

# 1.7 Geometric Manipulations: Sculpting Spatial Beauty
buffered_gdf = gdf.buffer(distance=1)

# 1.8 Set Operations with Overlay: Uniting and Distinguishing Spatial Tales
gdf1 = gpd.read_file('example1.geojson')
gdf2 = gpd.read_file('example2.geojson')
result = gpd.overlay(gdf1, gdf2, how='intersection')

# 1.9 Aggregation with Dissolve: Blending the Spatial Essence
gdf['category'] = ['cat1', 'cat2', 'cat1']
aggregated = gdf.dissolve(by='category')

# 1.10 Merging Data: Fusing Spatial Narratives
gdf1['key'] = ['A', 'B', 'C']
gdf2['key'] = ['B', 'A', 'C']
merged = gdf1.merge(gdf2, on='key')

# 1.11 Geocoding: Enchanting Addresses into Spatial Coordinates
geocoded = geocode("1600 Pennsylvania Ave NW, Washington, DC 20500", provider='nominatim')

# 1.12 Sampling Points: Capturing Spatial Essence with Delicacy
# Assuming that gdf's geometry column contains lines
gdf['geometry'] = pygeos.line_interpolate_point(gdf['geometry'], 0.5)

# 2. Advanced Guide: Unveiling the Hidden Gems

# 2.1 Missing and Empty Geometries: Navigating through the Unknown
missing_count = gdf['geometry'].isna().sum()

# 2.2 Re-projecting using GDAL with Rasterio and Fiona: Harmonizing Spatial Perspectives
with rasterio.open('example.tif') as src:
    transform, width, height = calculate_default_transform(src.crs, 'EPSG:4326', src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': 'EPSG:4326',
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open('output.tif', 'w', **kwargs) as dst:
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

# 2.3 Migration from PyGEOS geometry backend to Shapely 2.0: Embracing Evolution
pg_point = pygeos.points(0, 0)
shapely_point = Point(pg_point.to_wkt())

# 3. API Reference: Unraveling the Inner Workings

# 3.1 GeoSeries: Embracing the Symphony of Geometries
gs = gpd.GeoSeries([Point(0, 0), Point(1, 1), Point(2, 2)])
areas = gs.area

# 3.2 GeoDataFrame: Fusing Geometry and Tabular Beauty
gdf = gpd.GeoDataFrame({'geometry': gs})
total_area = gdf['geometry'].area.sum()

# 3.3 Input/Output: Unveiling the Gateway to Spatial Worlds
gdf.to_file('output.geojson', driver='GeoJSON')

# 3.4 Tools: Unleashing High-level Spatial Mastery
gdf1 = gpd.read_file('example1.geojson')
gdf2 = gpd.read_file('example2.geojson')
joined = gpd.sjoin(gdf1, gdf2, how='inner', op='intersects')

# 3.5 Spatial Index: Navigating the Spatial Labyrinth
sindex = gdf.sindex
possible_matches_index = list(sindex.intersection((1, 1, 2, 2)))
possible_matches = gdf.iloc[possible_matches_index]

# 3.6 Testing: Ensuring Spatial Harmony
# Run this in your command line interface, not in a Python script
# pytest --pyargs geopandas

# 4. Changelog: The Evolution of Spatial Elegance
# Visit the official GeoPandas documentation for the changelog

# Spatial poetry
"""
Remember, dear adventurer,
This poetic journey merely
Scratched GeoPandas' surface.
For comprehensive knowledge,
Refer to official documentation.
Let spatial poetry guide you
On the path of geospatial
Deep learning and innovation,
Where elegance intertwines
In harmonious bliss.
"""

