#building the image

docker build -t geospatial_minimal .

#inspired by @cordmaur

get docker image docker pull cordmaur/geospatial_minimal:latest
run container docker run -it --expose=8888 -p 8888:8888 cordmaur/geospatial_minimal
install jupyter pip install jupyter
run jupyter jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
