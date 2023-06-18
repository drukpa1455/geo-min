# GeoPandas: Explorando datos geoespaciales con elegancia y destreza

# Bienvenido al mundo encantador de GeoPandas,
# donde los datos geoespaciales cobran vida con elegancia y destreza.

# 1. Guía del Usuario: Desvelando el Núcleo

# Adentremos en nuestra exploración con la Guía del Usuario,
# que servirá como nuestra brújula a través del vasto reino de GeoPandas.
# Esta guía proporciona una descripción detallada de las funcionalidades principales
# y abre las puertas a un mundo de maravillas geoespaciales.

# 1.1 Estructuras de Datos: Uniendo Geometría y Datos Tabulares

# GeoPandas gira en torno a dos exquisitas estructuras de datos: GeoSeries y GeoDataFrame.
# Como una sinfonía de formas, GeoSeries es un vector que captura
# la esencia de cada observación a través de sus geometrías.
# Por otro lado, GeoDataFrame es una cautivadora estructura tabular
# que abraza a GeoSeries, dando vida a un conjunto de información espacial y atributiva.

# Permíteme mostrarte un ejemplo donde creamos un GeoDataFrame
# a partir de una colección de objetos Point de la librería Shapely:

# Crea un GeoSeries a partir de una lista de geometrías Point
gs = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])

# Crea un GeoDataFrame a partir del GeoSeries
gdf = gpd.GeoDataFrame({'geometry': gs})

# 1.2 Lectura y Escritura de Archivos: Abrazando las Narrativas Espaciales

# Las historias espaciales se cuentan a través de diversos formatos de archivos,
# y GeoPandas los valora a todos. Ya sea el encantador GeoJSON,
# el atemporal Shapefile o el mágico GeoPackage,
# GeoPandas lee y escribe datos geoespaciales en estos formatos con gracia.

# Únete a mí en un ejemplo donde leemos datos desde un cautivador archivo GeoJSON:

# Lee datos desde un archivo GeoJSON y crea un GeoDataFrame
gdf = gpd.read_file('ejemplo.geojson')

# 1.3 Indexación y Selección de Datos: Un Vistazo a las Maravillas Geométricas

# En el reino de GeoPandas, la indexación y selección de datos se despliegan como un baile encantador.
# Al igual que en pandas, podemos acceder y extraer con elegancia la esencia del conocimiento espacial.
# Desvelaremos un ejemplo donde seleccionamos la encantadora geometría de la primera fila en un GeoDataFrame:

# Accede a la geometría de la primera fila en el GeoDataFrame
primera_geometria = gdf.loc[0, 'geometry']

# 1.4 Creación de Mapas y Gráficos: Pintando el Mundo con Elegancia Espacial

# GeoPandas armoniza con el arte de Matplotlib
# para crear visualizaciones cautivadoras de datos geoespaciales.
# Un lienzo se despliega y las geometrías cobran vida en un gráfico cautivador.

# Experimenta la magia mientras creamos un gráfico básico de las geometrías en un GeoDataFrame:

# Grafica el GeoDataFrame
gdf.plot()

# 1.5 Mapas Interactivos: Desatando Relatos Espaciales con Interactividad

# GeoPandas abraza el poder de la web, entrelazándose con bibliotecas como Folium
# para tejer mapas interactivos. Juntos, podemos crear una experiencia inmersiva
# que cautiva y compromete.

# Únete a la aventura y crea un mapa interactivo utilizando Folium:

# Crea un mapa de Folium
m = folium.Map([51.5, -0.25], zoom_start=10)

# Agrega el GeoDataFrame al mapa de Folium
folium.GeoJson(gdf).add_to(m)

# 1.6 Proyecciones: Transformando Perspectivas, Iluminando el Mundo

# El mundo de los datos geoespaciales nos presenta diversos sistemas de referencia de coordenadas (CRS),
# cada uno iluminando la Tierra desde una perspectiva única.
# GeoPandas abraza esta diversidad y convierte sin esfuerzo entre diferentes CRS,
# permitiéndonos navegar el tapiz espacial.

# Presencia la transformación mientras convertimos un GeoDataFrame a un CRS diferente:

# Convierte el CRS del GeoDataFrame
gdf = gdf.to_crs(epsg=4326)

# 1.7 Manipulación Geométrica: Moldeando la Belleza Espacial

# En el reino de GeoPandas, podemos moldear y manipular las geometrías con el poder de Shapely.
# Este reino nos capacita para desatar una miríada de operaciones geométricas,
# creando maravillas espaciales.

# Permíteme presentarte un ejemplo donde creamos con gracia un buffer alrededor de cada geometría
# en un GeoDataFrame:

# Crea un buffer alrededor de cada geometría en el GeoDataFrame
buffered_gdf = gdf.buffer(distance=1)

# 1.8 Operaciones de Conjuntos con Overlay: Uniendo y Distinguiendo Relatos Espaciales

# Las operaciones de superposición nos permiten unir o distinguir
# los relatos contados por diferentes conjuntos de datos geoespaciales.
# GeoPandas ofrece un camino sin problemas para realizar operaciones de intersección, unión,
# diferencia y diferencia simétrica.

# Acompáñame en un viaje encantador donde intersectamos dos GeoDataFrames,
# tejiendo sus relatos en uno solo:

# Lee dos GeoDataFrames desde archivos GeoJSON
gdf1 = gpd.read_file('ejemplo1.geojson')
gdf2 = gpd.read_file('ejemplo2.geojson')

# Realiza una operación de intersección en los GeoDataFrames
resultado = gpd.overlay(gdf1, gdf2, how='intersection')

# 1.9 Agregación con Dissolve: Mezclando la Esencia Espacial

# En el reino de GeoPandas, podemos agregar datos espaciales,
# reuniendo entidades similares y mezclando sus atributos.
# Este proceso armonioso nos permite destilar la esencia del reino espacial.

# Acompáñame en un ejemplo donde agregamos basado en una columna 'categoría':

# Agrega una columna 'categoría' al GeoDataFrame
gdf['categoría'] = ['cat1', 'cat2', 'cat1']

# Realiza una operación de dissolve en el GeoDataFrame
agregado = gdf.dissolve(by='categoría')

# 1.10 Fusión de Datos: Entrelazando Relatos Espaciales

# La fusión de datos es un arte, y GeoPandas realza esta artesanía
# al manejar sin esfuerzo los datos espaciales.
# Acompáñame mientras fusionamos graciosamente dos GeoDataFrames, entrelazando sus relatos espaciales:

# Agrega una columna 'clave' a los GeoDataFrames
gdf1['clave'] = ['A', 'B', 'C']
gdf2['clave'] = ['B', 'A', 'C']

# Fusiona los GeoDataFrames basados en la columna 'clave'
fusionado = gdf1.merge(gdf2, on='clave')

# 1.11 Geocodificación: Transformando Direcciones en Coordenadas Espaciales

# La geocodificación trae el encanto de convertir direcciones en coordenadas geográficas,
# permitiéndonos colocar marcadores o ubicar el mapa.
# La geocodificación inversa da vida a las coordenadas geográficas,
# transformándolas en direcciones legibles para los humanos.

# Acompáñame en un ejemplo donde damos vida a una dirección a través de la geocodificación:

# Geocodifica una dirección y obtén las coordenadas espaciales correspondientes
geocodificado = geocode("1600 Pennsylvania Ave NW, Washington, DC 20500", provider='nominatim')

# 1.12 Muestreo de Puntos: Capturando la Esencia Espacial con Delicadeza

# El muestreo de puntos es una técnica artística, seleccionando cuidadosamente un subconjunto de datos para el análisis.
# Esta técnica mejora el rendimiento y acelera los cálculos
# cuando se trabaja con conjuntos de datos grandes.

# En el siguiente ejemplo, muestreamos un punto desde el corazón de cada línea
# en un GeoDataFrame, utilizando la mágica librería pygeos:

# Suponiendo que la columna 'geometry' del GeoDataFrame contiene líneas
gdf['geometry'] = pygeos.line_interpolate_point(gdf['geometry'], 0.5)

# 2. Guía Avanzada: Desvelando las Joyas Ocultas

# Ahora que hemos dominado el núcleo de GeoPandas,
# adentrémonos en la Guía Avanzada.
# Aquí, desvelamos joyas ocultas, explorando temas como el manejo de geometrías faltantes
# y vacías, reproyectando con la gracia de GDAL y Rasterio,
# y realizando una transición suave de PyGEOS a Shapely 2.0.

# 2.1 Geometrías Faltantes y Vacías: Navegando a través de lo Desconocido

# En el reino de los datos geoespaciales, a menudo nos encontramos con geometrías faltantes o vacías.
# GeoPandas nos equipa con las herramientas para manejar con gracia estas instancias.
# Descubramos un ejemplo donde identificamos filas con geometrías faltantes:

# Cuenta el número de geometrías faltantes en el GeoDataFrame
conteo_faltantes = gdf['geometry'].isna().sum()

# 2.2 Reproyección utilizando GDAL con Rasterio y Fiona: Armonizando Perspectivas Espaciales

# Rasterio y Fiona, los virtuosos de los datos raster y vectoriales geoespaciales,
# se unen con GDAL, el traductor de relatos espaciales.
# Juntos, desvelan el arte de reproyectar datos geoespaciales,
# permitiéndonos armonizar diferentes perspectivas.

# Acompáñame en un ejemplo donde reproyectamos un archivo raster con la elegancia de Rasterio:

# Abre el archivo raster utilizando Rasterio
with rasterio.open('ejemplo.tif') as fuente:
    # Calcula la transformación y dimensiones predeterminadas para la reproyección
    transformación, ancho, alto = calculate_default_transform(fuente.crs, 'EPSG:4326', fuente.width, fuente.height, *fuente.bounds)

    # Establece los metadatos para el archivo reproyectado
    kwargs = fuente.meta.copy()
    kwargs.update({
        'crs': 'EPSG:4326',
        'transform': transformación,
        'width': ancho,
        'height': alto
    })

    # Abre el archivo de destino para escribir
    with rasterio.open('salida.tif', 'w', **kwargs) as destino:
        # Realiza la reproyección para cada banda en el archivo fuente
        for i in range(1, fuente.count + 1):
            reproject(
                source=rasterio.band(fuente, i),
                destination=rasterio.band(destino, i),
                src_transform=fuente.transform,
                src_crs=fuente.crs,
                dst_transform=transformación,
                dst_crs='EPSG:4326',
                resampling=Resampling.nearest
            )

# 2.3 Migración de PyGEOS a Shapely 2.0: Abrazando la Evolución

# GeoPandas 0.8.0 introdujo la magia de PyGEOS,
# una librería que potencia las operaciones espaciales con sus funciones vectorizadas.
# Sin embargo, es esencial realizar una transición suave entre geometrías de PyGEOS y Shapely
# para trabajar en armonía con otras librerías de Python.

# Acompáñame en un ejemplo donde creamos con gracia una geometría utilizando PyGEOS
# y la convertimos a una geometría de Shapely:

# Crea una geometría Point utilizando PyGEOS
pg_point = pygeos.points(0, 0)

# Convierte la geometría de PyGEOS a una geometría de Shapely
shapely_point = Point(pg_point.to_wkt())

# 3. Referencia de la API: Desvelando los Entresijos

# Ahora, adentrémonos en las profundidades de la Referencia de la API,
# donde desvelamos los entresijos de GeoPandas.
# Descubre las complejidades de clases, métodos y atributos
# que tejen el tejido de GeoPandas.

# 3.1 GeoSeries: La Danza de las Geometrías

# GeoSeries, el corazón palpitante de GeoPandas,
# es una sucesión de geometrías cautivadoras.
# Estas geometrías danzan en armonía con métodos y atributos
# que tejen el tejido de GeoPandas.

# Permíteme mostrarte algunos métodos elegantes de GeoSeries:

# Calcula el área de cada geometría en el GeoSeries
areas = gs.area

# Encuentra la longitud del contorno de cada geometría en el GeoSeries
longitudes = gs.length

# 3.2 GeoDataFrame: El Telar de las Historias Geoespaciales

# GeoDataFrame es el telar donde se tejen las historias geoespaciales,
# con geometrías cautivadoras y atributos informativos.
# Sus métodos y atributos nos permiten explorar, transformar y analizar
# datos geoespaciales con elegancia.

# Permíteme mostrarte algunos métodos encantadores de GeoDataFrame:

# Filtra el GeoDataFrame para obtener solo las filas que cumplen con una condición
filtrado = gdf[gdf['columna'] > 10]

# Calcula el área total de todas las geometrías en el GeoDataFrame
area_total = gdf['geometry'].area.sum()

# ¡Y así concluye nuestra exploración en el reino de GeoPandas!
# Con elegancia y destreza, GeoPandas nos lleva de la mano
# a través de los encantos de los datos geoespaciales.
# Explora sus maravillas, crea tus propias rimas y desvela los secretos ocultos
# del mundo geoespacial con la gracia de un verdadero poeta.

