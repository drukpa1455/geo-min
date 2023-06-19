import urllib.request
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dask.array as da
import torch

# Overview
# 1.1 What is xarray?
# Xarray is a Python library for working with labeled multi-dimensional arrays and datasets. It provides a powerful and expressive API that enables efficient data manipulation, analysis, and visualization.

# 1.2 Why xarray?
# Xarray offers several advantages, including:
# - Label-based indexing and selection
# - Flexible handling of missing data
# - Seamless integration with pandas for tabular data
# - Support for parallel computing with Dask
# - Extensibility for integrating with other libraries

# Step 1: Download the dataset
url = 'https://www.ncei.noaa.gov/data/climate-indices/ersst.v5.1880-2021.nc'
file_path = 'ersst.v5.1880-2021.nc'
urllib.request.urlretrieve(url, file_path)

# Step 2: Load the dataset
ds = xr.open_dataset('ersst.v5.1880-2021.nc')

# Data Structures
# Dataset
# Access specific variables
sst = ds['sst']
anom = ds['anom']

# Access dimensions and coordinates
dims = ds.dims
coords = ds.coords

# DataArray
# Access specific variables
sst = ds['sst']
anom = ds['anom']

# Access dimensions and coordinates
dims = ds.dims
coords = ds.coords

# I/O
# Reading data (already covered in the Getting Started Guide)

# Writing data
# Saving the Dataset to a netCDF file
ds.to_netcdf('output.nc')

# Computation
# Operations
# Perform computations on variables
mean_sst = sst.mean(dim='time')
std_anom = anom.std(dim='time')

# Aggregations
# Perform aggregations on variables
max_sst = sst.max(dim='time')
min_anom = anom.min(dim='time')

# Broadcasting
# Broadcast variables to match dimensions
broadcasted = xr.broadcast(sst, anom)

# Plotting
# Basic Plotting
# Plot the mean sea surface temperature
mean_sst.plot()

# Add title and labels
plt.title('Mean Sea Surface Temperature')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()

# Advanced Plotting (not applicable in this example)

# User Guide
# Data Structures (already covered in the Getting Started Guide)

# Computation
# Missing Values / Fill Values
# Handle missing values
masked_sst = xr.where(sst > 0, sst, np.nan)

# Fill missing values with interpolation
filled_sst = masked_sst.interpolate_na(dim='time')

# GroupBy: Split, Apply, Combine
# Group by a specific dimension and calculate the mean
grouped_mean_sst = sst.groupby('time.month').mean()

# Resampling and grouped operations
# Resample the data to a different frequency
resampled_sst = sst.resample(time='Y').mean()

# Windowed operations
# Calculate a rolling mean over a time window
rolling_mean_sst = sst.rolling(time=12, center=True).mean()

# Rolling window operations (not applicable in this example)

# Plotting
# 1D Plots
# Line plot of the sea surface temperature
sst.plot.line(x='time')

# Histogram of the sea surface temperature
sst.plot.hist()

# 2D Plots
# Heatmap of the sea surface temperature
sst.plot.imshow()

# Contour plot of the sea surface temperature
sst.plot.contour()

# FacetGrid (not applicable in this example)

# Indexing and selecting data
# Label-based selection
# Select data based on specific coordinates
subset = sst.sel(lat=0, lon=slice(-180, -90))

# Position-based selection
# Select data based on positional indices
subset = sst.isel(lat=0, lon=slice(0, 100))

# Advanced indexing
# Select data based on boolean conditions
subset = sst.where(sst > 20, drop=True)

# Interpolation
# 1D Interpolation
# Interpolate data along a dimension
interpolated_sst = sst.interp(time=['2000-01-01', '2000-02-01'])

# Multi-dimensional Interpolation
# Interpolate data on a new grid
interpolated_grid = sst.interp(lat=[0, 10, 20], lon=[-120, -110, -100])

# Combining data
# Merge
# Merge two datasets
ds2 = xr.open_dataset('another_dataset.nc')
merged = xr.merge([ds, ds2])

# Concatenation
# Concatenate two datasets along a dimension
concatenated = xr.concat([ds, ds2], dim='time')

# Comparison
# Compare two datasets for equality
are_equal = ds.equals(ds2)

# Working with pandas
# Conversion to pandas objects
# Convert the Dataset to a pandas DataFrame
df = ds.to_dataframe()

# Conversion from pandas objects
# Convert a pandas DataFrame to a Dataset
ds_from_df = xr.Dataset.from_dataframe(df)

# Working with Dask
# Using dask arrays
# Create a Dask array from a NumPy array
numpy_array = np.random.rand(100, 100)
dask_array = da.from_array(numpy_array, chunks=(10, 10))

# Convert Dask array to xarray DataArray
xr_dataarray = xr.DataArray(dask_array)

# Performance and memory use (not applicable in this example)

# Using xarray with other libraries
# Interoperability
# Convert xarray Dataset to a PyTorch tensor
torch_tensor = torch.from_numpy(ds['sst'].values)

# Extending xarray
# Create a custom xarray accessor
@xr.register_dataarray_accessor('custom')
class CustomAccessor:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def custom_method(self):
        # Implement your custom method logic here
        pass

# Use the custom accessor on an xarray DataArray
custom_dataarray = ds['sst'].custom.custom_method()

# Close the dataset
ds.close()
