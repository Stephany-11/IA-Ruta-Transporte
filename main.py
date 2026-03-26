import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

# Cargar el GeoDataFrame desde el archivo GeoJSON
gdf = gpd.read_file('Estaciones.geojson')

