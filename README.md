# IA-Ruta-Transporte
Proyecto de Rutas en Redes de Estaciones Troncales
Este proyecto tiene como objetivo crear y visualizar una red de estaciones utilizando datos geográficos y el paquete NetworkX para la creación y análisis de grafos. Se utiliza un archivo GeoJSON que contiene las estaciones y sus coordenadas para construir el grafo y calcular la ruta más corta entre dos estaciones.

Contenido del Proyecto
Estaciones_troncales.geojson: Archivo que contiene la información geográfica de las estaciones, incluyendo:

objectid: Identificador único para cada estación y usado para definir el orden.
nombre_estacion: Nombre de la estación.
coordenada_x_estacion y coordenada_y_estacion: Coordenadas de la estación.
La geometría de cada estación en formato GeoJSON (tipo Point).
