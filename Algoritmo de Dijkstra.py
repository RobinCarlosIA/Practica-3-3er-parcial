# Algoritmo de Dijkstra
# Este programa encuentra el camino más corto desde un nodo inicial a todos los demás en un grafo.
# Hecho por [Tu Nombre]

import heapq  # Biblioteca para manejar la cola de prioridad
import matplotlib.pyplot as plt  # Para la parte gráfica
import networkx as nx  # Para visualizar el grafo

# Función del Algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    """
    Calcula los caminos más cortos desde un nodo inicial a todos los demás.
    """
    # Creamos un diccionario con las distancias iniciales. Todas son "infinitas" menos el nodo inicial, que es 0.
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Creamos una cola de prioridad para procesar los nodos. Guardamos la distancia y el nodo.
    cola_prioridad = [(0, inicio)]

    # Guardamos los caminos más cortos hacia cada nodo
    caminos = {inicio: [inicio]}

    # Imprimimos el estado inicial
    print(f"Iniciamos el cálculo desde el nodo '{inicio}'\n")

    # Mientras tengamos nodos por procesar
    while cola_prioridad:
        # Sacamos el nodo con la distancia más corta de la cola
        dist_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Imprimimos el nodo que estamos procesando
        print(f"Procesando nodo '{nodo_actual}' con distancia acumulada: {dist_actual}")

        # Recorremos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            # Calculamos la nueva distancia al vecino
            nueva_distancia = dist_actual + peso

            # Si encontramos una distancia más corta, actualizamos
            if nueva_distancia < distancias[vecino]:
                print(f"  Actualizando nodo '{vecino}': distancia anterior {distancias[vecino]}, nueva distancia {nueva_distancia}")
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                caminos[vecino] = caminos[nodo_actual] + [vecino]  # Actualizamos el camino más corto

    # Retornamos las distancias y los caminos
    print("\nCálculo completado.\n")
    return distancias, caminos

# Función para dibujar el grafo y los caminos más cortos
def dibujar_grafo(grafo, caminos, nodo_inicio):
    """
    Muestra gráficamente el grafo y resalta los caminos más cortos.
    """
    # Crear el grafo con NetworkX
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    # Configuramos la posición de los nodos
    posiciones = nx.spring_layout(G)
    pesos_aristas = nx.get_edge_attributes(G, 'weight')

    # Dibujamos el grafo completo
    plt.figure(figsize=(10, 6))
    nx.draw(G, posiciones, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, posiciones, edge_labels=pesos_aristas)

    # Resaltamos los caminos más cortos
    for nodo, camino in caminos.items():
        if nodo != nodo_inicio:  # No resaltamos el nodo inicial
            aristas = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
            nx.draw_networkx_edges(G, posiciones, edgelist=aristas, edge_color="red", width=2)

    # Mostramos la gráfica
    plt.title(f"Caminos más cortos desde '{nodo_inicio}'")
    plt.show()

# Definimos el grafo como un diccionario
grafo = {
    'R': {'E': 2, 'C': 4},
    'E': {'R': 2, 'G': 7, 'F': 3},
    'C': {'R': 4, 'F': 1, 'D': 5},
    'G': {'E': 7, 'D': 2},
    'F': {'E': 3, 'C': 1, 'B': 8},
    'D': {'C': 5, 'G': 2, 'B': 6},
    'B': {'F': 8, 'D': 6}
}

# Nodo inicial
nodo_inicio = 'R'

# Llamamos al algoritmo de Dijkstra
print("=== Algoritmo de Dijkstra ===\n")
distancias, caminos = dijkstra(grafo, nodo_inicio)

# Mostramos los resultados
print("\nDistancias más cortas desde el nodo inicial:")
for nodo, distancia in distancias.items():
    print(f"  {nodo}: {distancia}")

print("\nCaminos más cortos desde el nodo inicial:")
for nodo, camino in caminos.items():
    print(f"  {nodo}: {' -> '.join(camino)}")

# Dibujamos el grafo con los caminos más cortos
dibujar_grafo(grafo, caminos, nodo_inicio)

