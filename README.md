# geo_min
minimal docker image for geospatial analysis with python

# building the image
`docker build -t geospatial_minimal .`

# inspired by @cordmaur
1. get docker image
`docker pull cordmaur/geospatial_minimal:latest`
2. run container
`docker run -it --expose=8888 -p 8888:8888 cordmaur/geospatial_minimal`
3. install lab
pip install jupyterlab
4. jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
