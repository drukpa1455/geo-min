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

import geopandas as gpd
from shapely.geometry import Point
import folium
from geopandas.tools import geocode
import pygeos
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

# GeoPandas: Exploring Geospatial Data with Elegance and Ease

# Welcome to the enchanting world of GeoPandas,
# where geospatial data comes alive with elegance and ease.

# 1. User Guide: Unveiling the Core

# Let us begin our exploration with the User Guide,
# which serves as our compass through the vast realm of GeoPandas.
# This guide provides a detailed walkthrough of the core functionalities
# and opens the doors to a multitude of geospatial wonders.

# 1.1 Data Structures: Uniting Geometry and Tabular Data

# GeoPandas revolves around two exquisite data structures: GeoSeries and GeoDataFrame.
# Just like a symphony of shapes, a GeoSeries is a vector that captures
# the essence of each observation through its geometries.
# A GeoDataFrame, on the other hand, is a captivating tabular structure
# that embraces a GeoSeries, giving life to an ensemble of spatial and attribute information.

# Let's craft an example together, where we weave a GeoDataFrame
# from a collection of Shapely Point objects:

# Create a GeoSeries from a list of Point geometries
gs = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])

# Create a GeoDataFrame from the GeoSeries
gdf = gpd.GeoDataFrame({'geometry': gs})

# 1.2 Reading and Writing Files: Embracing the Spatial Narratives

# Spatial stories are often told through various file formats,
# and GeoPandas cherishes them all. Whether it's the enchanting GeoJSON,
# the timeless Shapefile, or the magical GeoPackage,
# GeoPandas gracefully reads and writes geospatial data from and to these formats.

# Join me in a mesmerizing example where we read data from a captivating GeoJSON file:

# Read data from a GeoJSON file and create a GeoDataFrame
gdf = gpd.read_file('example.geojson')

# 1.3 Indexing and Selecting Data: A Glimpse of Geometric Wonders

# In the realm of GeoPandas, indexing and selecting data unfolds like a cherished dance.
# Just as in pandas, we can elegantly access and extract the essence of spatial knowledge.
# Let's unveil an example where we select the enchanting geometry of the first row in a GeoDataFrame:

# Access the geometry of the first row in the GeoDataFrame
first_geometry = gdf.loc[0, 'geometry']

# 1.4 Making Maps and Plots: Painting the World with Spatial Elegance

# GeoPandas harmonizes with the artistic prowess of Matplotlib
# to create mesmerizing visualizations of geospatial data.
# A canvas unfolds, and the geometries come to life in a captivating plot.

# Experience the magic as we create a basic plot of the geometries in a GeoDataFrame:

# Plot the GeoDataFrame
gdf.plot()

# 1.5 Interactive Mapping: Unleashing Spatial Tales with Interactivity

# GeoPandas embraces the power of the web, intertwining with libraries like Folium
# to weave interactive maps. Together, we can craft an immersive experience
# that engages and captivates.

# Let's embark on an adventure and create an interactive map using Folium:

# Create a Folium map
m = folium.Map([51.5, -0.25], zoom_start=10)

# Add the GeoDataFrame to the Folium map
folium.GeoJson(gdf).add_to(m)

# 1.6 Projections: Transforming Perspectives, Illuminating the World

# The world of geospatial data presents us with diverse coordinate reference systems (CRS),
# each illuminating the Earth from a unique vantage point.
# GeoPandas embraces this diversity and effortlessly converts between different CRS,
# allowing us to navigate the spatial tapestry.

# Witness the transformation as we convert a GeoDataFrame to a different CRS:

# Convert the CRS of the GeoDataFrame
gdf = gdf.to_crs(epsg=4326)

# 1.7 Geometric Manipulations: Sculpting Spatial Beauty

# In the realm of GeoPandas, we can mold and shape the geometries with the power of Shapely.
# This realm empowers us to unleash a myriad of geometric operations,
# creating spatial wonders.

# Let's bring forth an example where we gracefully create a buffer around each geometry
# in a GeoDataFrame:

# Create a buffer around each geometry in the GeoDataFrame
buffered_gdf = gdf.buffer(distance=1)

# 1.8 Set Operations with Overlay: Uniting and Distinguishing Spatial Tales

# Overlay operations allow us to bring together or differentiate
# the stories told by different geospatial datasets.
# GeoPandas offers a seamless path to perform intersection, union, difference,
# and symmetric difference operations.

# Let's embark on an enchanting journey where we intersect two GeoDataFrames,
# weaving their tales into one:

# Read two GeoDataFrames from GeoJSON files
gdf1 = gpd.read_file('example1.geojson')
gdf2 = gpd.read_file('example2.geojson')

# Perform an intersection operation on the GeoDataFrames
result = gpd.overlay(gdf1, gdf2, how='intersection')

# 1.9 Aggregation with Dissolve: Blending the Spatial Essence

# In the realm of GeoPandas, we can aggregate spatial data,
# bringing together similar entities and blending their attributes.
# This harmonious process allows us to distill the essence of the spatial realm.

# Let's embark on an example where we aggregate based on a 'category' column:

# Add a 'category' column to the GeoDataFrame
gdf['category'] = ['cat1', 'cat2', 'cat1']

# Perform a dissolve operation on the GeoDataFrame
aggregated = gdf.dissolve(by='category')

# 1.10 Merging Data: Fusing Spatial Narratives

# Merging data is an art, and GeoPandas enhances this artistry
# by seamlessly handling spatial data.
# Join me as we gracefully merge two GeoDataFrames, intertwining their spatial tales:

# Add a 'key' column to the GeoDataFrames
gdf1['key'] = ['A', 'B', 'C']
gdf2['key'] = ['B', 'A', 'C']

# Merge the GeoDataFrames based on the 'key' column
merged = gdf1.merge(gdf2, on='key')

# 1.11 Geocoding: Enchanting Addresses into Spatial Coordinates

# Geocoding brings the enchantment of converting addresses into geographic coordinates,
# allowing us to place markers or position the map.
# Reverse geocoding breathes life into geographic coordinates,
# transforming them into human-readable addresses.

# Join me as we embark on an example where we bring an address to life through geocoding:

# Geocode an address and retrieve the corresponding spatial coordinates
geocoded = geocode("1600 Pennsylvania Ave NW, Washington, DC 20500", provider='nominatim')

# 1.12 Sampling Points: Capturing Spatial Essence with Delicacy

# Sampling points is an artful technique, delicately selecting a subset of data for analysis.
# This technique gracefully enhances performance and expedites computations
# when working with large datasets.

# In the following example, we sample a point from the heart of each line
# in a GeoDataFrame, using the magical pygeos library:

# Assuming that gdf's geometry column contains lines
gdf['geometry'] = pygeos.line_interpolate_point(gdf['geometry'], 0.5)

# 2. Advanced Guide: Unveiling the Hidden Gems

# Now that we have mastered the core of GeoPandas,
# let us delve into the Advanced Guide.
# Here, we uncover hidden gems, exploring topics such as handling missing
# and empty geometries, re-projecting with the grace of GDAL and Rasterio,
# and gracefully migrating from PyGEOS to Shapely 2.0.

# 2.1 Missing and Empty Geometries: Navigating through the Unknown

# In the realm of geospatial data, we often encounter missing or empty geometries.
# GeoPandas equips us with the tools to gracefully handle these instances.
# Let us uncover an example where we identify rows with missing geometries:

# Count the number of missing geometries in the GeoDataFrame
missing_count = gdf['geometry'].isna().sum()

# 2.2 Re-projecting using GDAL with Rasterio and Fiona: Harmonizing Spatial Perspectives

# Rasterio and Fiona, the virtuosos of geospatial raster and vector data,
# join hands with GDAL, the translator of spatial tales.
# Together, they unveil the art of re-projecting geospatial data,
# allowing us to harmonize different perspectives.

# Join me in an example where we re-project a raster file with the elegance of Rasterio:

# Open the raster file using Rasterio
with rasterio.open('example.tif') as src:
    # Calculate the default transformation and dimensions for re-projection
    transform, width, height = calculate_default_transform(src.crs, 'EPSG:4326', src.width, src.height, *src.bounds)

    # Set the metadata for the re-projected file
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': 'EPSG:4326',
        'transform': transform,
        'width': width,
        'height': height
    })

    # Open the destination file for writing
    with rasterio.open('output.tif', 'w', **kwargs) as dst:
        # Perform the re-projection for each band in the source file
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

# GeoPandas 0.8.0 introduced the magic of PyGEOS,
# a library that amplifies spatial operations with its vectorized functions.
# Yet, it is essential to gracefully transition between PyGEOS and Shapely geometries
# to work harmoniously with other Python libraries.

# Join me in an example where we gracefully create a geometry using PyGEOS
# and convert it to a Shapely geometry:

# Create a Point geometry using PyGEOS
pg_point = pygeos.points(0, 0)

# Convert the PyGEOS geometry to a Shapely geometry
shapely_point = Point(pg_point.to_wkt())

# 3. API Reference: Unraveling the Inner Workings

# Now, let us journey into the depths of the API Reference,
# where we unravel the inner workings of GeoPandas.
# Discover the intricacies of classes, methods, and attributes
# that weave the fabric of GeoPandas.

# 3.1 GeoSeries: Embracing the Symphony of Geometries

# A GeoSeries dances to the rhythm of geometries,
# a captivating one-dimensional array that can store various geometric objects.
# Join me in an example where we create a GeoSeries
# and embark on a journey to calculate the area of each geometry:

# Create a GeoSeries with Point geometries
gs = gpd.GeoSeries([Point(0, 0), Point(1, 1), Point(2, 2)])

# Calculate the area of each geometry in the GeoSeries
areas = gs.area

# 3.2 GeoDataFrame: Fusing Geometry and Tabular Beauty

# A GeoDataFrame is a harmonious union of a pandas DataFrame
# and the grace of geospatial data.
# With this captivating data structure, we can navigate
# the world of spatial and attribute information with ease.

# In this example, we create a GeoDataFrame and embark on a journey
# to calculate the total area:

# Create a GeoDataFrame from the GeoSeries
gdf = gpd.GeoDataFrame({'geometry': gs})

# Calculate the total area of all geometries in the GeoDataFrame
total_area = gdf['geometry'].area.sum()

# 3.3 Input/Output: Unveiling the Gateway to Spatial Worlds

# GeoPandas gracefully communicates with various file formats,
# enabling the seamless exchange of spatial narratives.
# Discover the enchanting power as we write a GeoDataFrame to a GeoJSON file:

# Write the GeoDataFrame to a GeoJSON file
gdf.to_file('output.geojson', driver='GeoJSON')

# 3.4 Tools: Unleashing High-level Spatial Mastery

# GeoPandas provides us with high-level tools,
# allowing us to perform sophisticated spatial operations with elegance.
# Let's embark on an adventure where we perform a spatial join between two GeoDataFrames:

# Read two GeoDataFrames from GeoJSON files
gdf1 = gpd.read_file('example1.geojson')
gdf2 = gpd.read_file('example2.geojson')

# Perform a spatial join operation on the GeoDataFrames
joined = gpd.sjoin(gdf1, gdf2, how='inner', op='intersects')

# 3.5 Spatial Index: Navigating the Spatial Labyrinth

# In the vast labyrinth of spatial data, a spatial index becomes our guide.
# GeoPandas empowers us with the ability to perform fast spatial queries
# using spatial indices.

# Let's traverse this labyrinth together in an example
# where we query a GeoDataFrame using a spatial index:

# Create a spatial index for the GeoDataFrame
sindex = gdf.sindex

# Find the possible matches within a bounding box
possible_matches_index = list(sindex.intersection((1, 1, 2, 2)))

# Retrieve the possible matches from the GeoDataFrame
possible_matches = gdf.iloc[possible_matches_index]

# 3.6 Testing: Ensuring Spatial Harmony

# GeoPandas takes pride in its tests, ensuring the stability
# and reliability of its spatial harmonies.
# Join us as we unveil the art of running the GeoPandas test suite,
# ensuring the continuation of spatial magic:

# Run the GeoPandas test suite
# Run this in your command line interface, not in a Python script
# pytest --pyargs geopandas

# 4. Changelog: The Evolution of Spatial Elegance

# As we embrace the evolving nature of GeoPandas,
# let us turn our attention to the Changelog.
# Here, we discover the changes introduced in each version,
# ensuring that we remain in sync with the latest spatial wonders.

# Spatial poetry
"""
Remember, dear adventurer,
This poetic journey has merely scratched the surface
Of GeoPandas' enchantments.
For comprehensive and up-to-date knowledge,
Always refer to the official GeoPandas documentation.
Let the spatial poetry guide you on your path of geospatial deep learning,
Where elegance and innovation intertwine in harmonious bliss.
"""

# Let your geospatial exploration begin!
