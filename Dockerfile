# Use an official GDAL image as the base image
FROM osgeo/gdal:ubuntu-small-latest

# Install PIP
RUN apt-get update && apt-get -y install python3-pip --fix-missing


