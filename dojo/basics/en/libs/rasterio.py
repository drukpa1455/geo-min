import numpy as np  # Import numpy for array manipulation
import rasterio  # Import rasterio for raster data processing
from rasterio.features import shapes  # Import shapes to generate vector shapes from raster data
from rasterio.windows import Window  # Import Window for windowed operations
from rasterio.warp import calculate_default_transform, reproject, Resampling  # Import functions for reprojection
from rasterio.merge import merge  # Import merge function to merge raster datasets
import matplotlib.pyplot as plt  # Import matplotlib for data visualization

def main():
    # Open the raster file
    with rasterio.open('example.tif') as src:  # 'src' is now a DatasetReader object
        print(src.profile)  # Print the profile (meta-data) of the raster

    # Read the first band of the raster file
    with rasterio.open('example.tif') as src:
        band1 = src.read(1)  # Read the first band

    # Write raster data
    array = np.random.randint(0, 255, (3, 300, 300)).astype(np.uint8)  # Generate a random 3-band raster array
    profile = {'driver':'GTiff', 'height':300, 'width':300, 'count':3, 'dtype':rasterio.uint8}  # Define the profile for the new raster

    with rasterio.open('output.tif', 'w', **profile) as dst:  # Open a new raster file for writing
        dst.write(array)  # Write the array to the raster

    # Read the first band and its associated mask
    with rasterio.open('example.tif') as src:
        band1 = src.read(1)  # Read the first band
        mask = src.read_masks(1)  # Read the associated mask

    # Print the data types of the bands and their color interpretations
    with rasterio.open('example.tif') as src:
        print(src.dtypes)  # Print the data types of the bands
        print(src.colorinterp)  # Print the color interpretations

    # Print the coordinate reference system of the raster
    with rasterio.open('example.tif') as src:
        print(src.crs)  # Print the CRS

    # Generate vector shapes from the raster values
    mask = None  # Define a mask (none in this case)
    with rasterio.open('example.tif') as src:
        image = src.read(1)  # Read the first band
        results = (
        {'properties': {'raster_val': v}, 'geometry': s}  # Generate a dict with raster values and geometry
        for i, (s, v) 
        in enumerate(shapes(image, mask=mask, transform=src.transform)))  # Enumerate through shapes

    # Print the meta-data profile of the raster
    with rasterio.open('example.tif') as src:
        print(src.profile)  # Print the profile

    # Read a subset of the raster file
    with rasterio.open('example.tif') as src:
        subset = src.read(1, window=Window(0, 0, 10, 10))  # Read a subset defined by the window

    # Read a raster file into a numpy array
    with rasterio.open('example.tif') as src:
        image = src.read()  # The raster data is now a numpy array

    # Merge two raster datasets into a single mosaic
    src1 = rasterio.open('image1.tif')  # Open the first raster file
    src2 = rasterio.open('image2.tif')  # Open the second raster file
    mosaic, out_trans = merge([src1, src2])  # Merge the two rasters

    # Plot the first band of a raster file using matplotlib
    with rasterio.open('example.tif') as src:
        image = src.read(1)  # Read the first band
    plt.imshow(image)  # Display the band as an image
    plt.show()  # Show the plot

    # Reproject a raster to a different coordinate reference system
    dst_crs = 'EPSG:4326'  # Define the new CRS
    with rasterio.open('example.tif') as src:
        transform, width, height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds)  # Calculate the default transform for the reprojection
        kwargs = src.meta.copy()  # Copy the meta-data of the original raster
        kwargs.update({
            'crs': dst_crs,  # Update the CRS
            'transform': transform,  # Update the transform
            'width': width,  # Update the width
            'height': height  # Update the height
        })

        with rasterio.open('output.tif', 'w', **kwargs) as dst:  # Open a new raster file for writing
            for i in range(1, src.count + 1):  # Loop through each band
                reproject(
                    source=rasterio.band(src, i),  # Define the source band
                    destination=rasterio.band(dst, i),  # Define the destination band
                    src_transform=src.transform,  # Define the source transform
                    src_crs=src.crs,  # Define the source CRS
                    dst_transform=transform,  # Define the destination transform
                    dst_crs=dst_crs,  # Define the destination CRS
                    resampling=Resampling.nearest)  # Define the resampling method

if __name__ == "__main__":
    main()  # Call the main function when the script is run directly
