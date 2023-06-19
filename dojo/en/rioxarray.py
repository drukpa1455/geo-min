# rioxarray 0.14.0 Documentation

import os
import wget
import zipfile
import rioxarray
import xarray as xr
import matplotlib.pyplot as plt
from shapely.geometry import box

# Downloading a sample dataset
file_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/HYP_LR.tif.zip"
file_path = "./HYP_LR.tif.zip"
wget.download(file_url, file_path)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall("./")
tif_file = "./HYP_LR.tif"

# Opening raster data with rioxarray
rds = rioxarray.open_rasterio(tif_file)

# 2.3.3. Managing Information Loss with xarray operations
# Some xarray operations drop attributes, you can use assign_attrs to reassign them.
mean_rds = rds.mean(dim="x").assign_attrs(rds.attrs)
print(mean_rds)

# 4.4. rioxarray.show_versions
# To check the versions of rioxarray and its dependencies
rioxarray.show_versions()

# Using rioxarray for geospatial operations - Clipping
# Create a geometry (in this case a box) in the same CRS as the rioxarray dataset
clipping_box = box(minx=-30, miny=-20, maxx=40, maxy=20)

# Then use the clip method on the rioxarray dataset object
clipped = rds.rio.clip([clipping_box])

# Plot the clipped raster
clipped.plot()
plt.show()

# Reprojecting
# Use the reproject method to change the CRS of the raster data
reprojected = rds.rio.reproject("EPSG:4326")

# Plot the reprojected raster
reprojected.plot()
plt.show()

# Resampling
# Resample the raster data to a lower resolution
resampled = rds.rio.reproject(rds.rio.crs, resolution=(2, 2))

# Plot the resampled raster
resampled.plot()
plt.show()

# Saving a raster to disk
# Save the raster data to a new GeoTIFF file
reprojected.rio.to_raster("reprojected.tif")
