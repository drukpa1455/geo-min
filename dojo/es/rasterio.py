import numpy as np  # Importa numpy para la manipulación de matrices
import rasterio  # Importa rasterio para el procesamiento de datos raster
from rasterio.features import shapes  # Importa shapes para generar formas vectoriales a partir de datos raster
from rasterio.windows import Window  # Importa Window para operaciones con ventanas
from rasterio.warp import calculate_default_transform, reproject, Resampling  # Importa funciones para la reproyección
from rasterio.merge import merge  # Importa la función merge para unir conjuntos de datos raster
import matplotlib.pyplot as plt  # Importa matplotlib para la visualización de datos

def main():
    # Abre el archivo raster
    with rasterio.open('example.tif') as src:  # 'src' es ahora un objeto DatasetReader
        print(src.profile)  # Imprime el perfil (metadatos) del raster

    # Lee la primera banda del archivo raster
    with rasterio.open('example.tif') as src:
        banda1 = src.read(1)  # Lee la primera banda

    # Escribe datos raster
    matriz = np.random.randint(0, 255, (3, 300, 300)).astype(np.uint8)  # Genera una matriz raster de 3 bandas aleatoria
    perfil = {'driver':'GTiff', 'height':300, 'width':300, 'count':3, 'dtype':rasterio.uint8}  # Define el perfil para el nuevo raster

    with rasterio.open('output.tif', 'w', **perfil) as dst:  # Abre un nuevo archivo raster para escribir
        dst.write(matriz)  # Escribe la matriz en el raster

    # Lee la primera banda y su máscara asociada
    with rasterio.open('example.tif') as src:
        banda1 = src.read(1)  # Lee la primera banda
        mascara = src.read_masks(1)  # Lee la máscara asociada

    # Imprime los tipos de datos de las bandas y sus interpretaciones de color
    with rasterio.open('example.tif') as src:
        print(src.dtypes)  # Imprime los tipos de datos de las bandas
        print(src.colorinterp)  # Imprime las interpretaciones de color

    # Imprime el sistema de referencia de coordenadas del raster
    with rasterio.open('example.tif') as src:
        print(src.crs)  # Imprime el SRC

    # Genera formas vectoriales a partir de los valores del raster
    mascara = None  # Define una máscara (ninguna en este caso)
    with rasterio.open('example.tif') as src:
        imagen = src.read(1)  # Lee la primera banda
        resultados = (
        {'properties': {'raster_val': v}, 'geometry': s}  # Genera un diccionario con los valores del raster y la geometría
        for i, (s, v) 
        in enumerate(shapes(imagen, mask=mascara, transform=src.transform)))  # Enumera a través de las formas

    # Imprime el perfil (metadatos) del raster
    with rasterio.open('example.tif') as src:
        print(src.profile)  # Imprime el perfil

    # Lee un subconjunto del archivo raster
    with rasterio.open('example.tif') as src:
        subconjunto = src.read(1, window=Window(0, 0, 10, 10))  # Lee un subconjunto definido por la ventana

    # Lee un archivo raster en una matriz de numpy
    with rasterio.open('example.tif') as src:
        imagen = src.read()  # Los datos del raster son ahora una matriz de numpy

    # Une dos conjuntos de datos raster en un mosaico único
    src1 = rasterio.open('image1.tif')  # Abre el primer raster
    src2 = rasterio.open('image2.tif')  # Abre el segundo raster
    mosaico, trans_out = merge([src1, src2])  # Une los dos rasters

    # Dibuja la primera banda de un archivo raster usando matplotlib
    with rasterio.open('example.tif') as src:
        imagen = src.read(1)  # Lee la primera banda
    plt.imshow(imagen)  # Muestra la banda como una imagen
    plt.show()  # Muestra la trama

    # Re-proyecta un raster a un sistema de referencia de coordenadas diferente
    dst_crs = 'EPSG:4326'  # Define el nuevo SRC
    with rasterio.open('example.tif') as src:
        transform, width, height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds)  # Calcula la transformación por defecto para la reproyección
        kwargs = src.meta.copy()  # Copia los metadatos del raster original
        kwargs.update({
            'crs': dst_crs,  # Actualiza el SRC
            'transform': transform,  # Actualiza la transformación
            'width': width,  # Actualiza el ancho
            'height': height  # Actualiza la altura
        })

        with rasterio.open('output.tif', 'w', **kwargs) as dst:  # Abre un nuevo archivo raster para escribir
            for i in range(1, src.count + 1):  # Recorre cada banda
                reproject(
                    source=rasterio.band(src, i),  # Define la banda fuente
                    destination=rasterio.band(dst, i),  # Define la banda de destino
                    src_transform=src.transform,  # Define la transformación de origen
                    src_crs=src.crs,  # Define el SRC de origen
                    dst_transform=transform,  # Define la transformación de destino
                    dst_crs=dst_crs,  # Define el SRC de destino
                    resampling=Resampling.nearest)  # Define el método de remuestreo

if __name__ == "__main__":
    main()  # Llama a la función principal cuando el script se ejecuta directamente
