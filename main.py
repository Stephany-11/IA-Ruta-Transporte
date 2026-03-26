import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

# Cargar el GeoDataFrame desde el archivo GeoJSON
gdf = gpd.read_file(
    r'C:\Users\Usuario\Desktop\proyecto\Estaciones_Troncales_de_TRANSMILEND.geojson'
)

# Crear un grafo de NetworkX
G = nx.Graph()

# Añadir los nodos (cada estación) basados en los datos del GeoDataFrame
for index, row in gdf.iterrows():
    nombre_estacion = row["nombre_estacion"]
    pos = (row["coordenada_x_estacion"], row["coordenada_y_estacion"])
    G.add_node(nombre_estacion, pos=pos)

# Ordenar por alguna columna que permita conectar las estaciones en secuencia (por ejemplo, "objectid")
troncales_ordenadas = gdf.sort_values('objectid')

# Crear las conexiones secuenciales entre estaciones (asumiendo que la columna 'objectid' define un orden)
for i in range(len(troncales_ordenadas) - 1):
    estacion_actual = troncales_ordenadas.iloc[i]["nombre_estacion"]
    estacion_siguiente = troncales_ordenadas.iloc[i+1]["nombre_estacion"]
    G.add_edge(estacion_actual, estacion_siguiente)

# (Opcional) Aquí podrías añadir conexiones específicas entre estaciones, si se conocen,
# por ejemplo: G.add_edge("EstaciónX", "EstaciónY")

# Función para encontrar la ruta más corta usando Dijkstra o BFS (por defecto, shortest_path de NetworkX)
def encontrar_ruta_mas_corta(origen, destino):
    try:
        ruta = nx.shortest_path(G, source=origen, target=destino)
        return ruta
    except nx.NetworkXNoPath:
        return "No hay ruta disponible entre las estaciones seleccionadas."

# Ejemplo de uso
origen = "Alcalá"
destino = "Portal Norte"
ruta_mas_corta = encontrar_ruta_mas_corta(origen, destino)
print("La ruta más corta es:", ruta_mas_corta)

# Visualización básica del grafo
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=50, font_size=8)
plt.show()