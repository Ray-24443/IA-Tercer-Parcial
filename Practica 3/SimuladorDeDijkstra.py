# ============================================================
# SIMULADOR DEL ALGORITMO DE DIJKSTRA
# Muestra paso a paso en consola y genera una gráfica del grafo
# ============================================================

# Importamos la cola de prioridad
import heapq

# Importamos NetworkX para crear el grafo
import networkx as nx

# Importamos Matplotlib para mostrar la gráfica
import matplotlib.pyplot as plt


# ============================================================
# FUNCIÓN DEL ALGORITMO DE DIJKSTRA
# ============================================================

def dijkstra_paso_a_paso(grafo, inicio):

    # Diccionario de distancias
    distancias = {}

    # Inicializamos todas las distancias en infinito
    for nodo in grafo:
        distancias[nodo] = float('inf')

    # La distancia al nodo inicial es cero
    distancias[inicio] = 0

    # Cola de prioridad
    cola = [(0, inicio)]

    # Contador de pasos
    paso = 1

    print("\n================================================")
    print("      INICIO DEL ALGORITMO DE DIJKSTRA")
    print("================================================")

    # Mientras existan nodos por procesar
    while cola:

        print(f"\nPASO {paso}")

        # Extraemos el nodo con menor distancia
        distancia_actual, nodo_actual = heapq.heappop(cola)

        print(f"Nodo seleccionado: {nodo_actual}")
        print(f"Distancia acumulada: {distancia_actual}")

        # Analizamos todos los vecinos
        for vecino, peso in grafo[nodo_actual]:

            print(f"\nAnalizando vecino: {vecino}")

            nueva_distancia = distancia_actual + peso

            print(
                f"Distancia calculada = "
                f"{distancia_actual} + {peso} = {nueva_distancia}"
            )

            # Si encontramos una mejor ruta
            if nueva_distancia < distancias[vecino]:

                print("Se encontró una ruta más corta")

                print(
                    f"Distancia anterior: "
                    f"{distancias[vecino]}"
                )

                distancias[vecino] = nueva_distancia

                print(
                    f"Nueva distancia: "
                    f"{distancias[vecino]}"
                )

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

            else:

                print(
                    "No mejora la distancia existente"
                )

        print("\nTabla de distancias:")

        for nodo in distancias:
            print(f"{nodo}: {distancias[nodo]}")

        input("\nPresione ENTER para continuar...")

        paso += 1

    print("\n================================================")
    print("              RESULTADO FINAL")
    print("================================================")

    for nodo in distancias:
        print(
            f"Distancia mínima desde "
            f"{inicio} hasta {nodo}: "
            f"{distancias[nodo]}"
        )

    return distancias


# ============================================================
# FUNCIÓN PARA GRAFICAR EL GRAFO
# ============================================================

def graficar_grafo(grafo):

    # Creamos un grafo vacío
    G = nx.Graph()

    # Agregamos las conexiones
    for nodo in grafo:

        for vecino, peso in grafo[nodo]:

            G.add_edge(
                nodo,
                vecino,
                weight=peso
            )

    # Posición automática de los nodos
    pos = nx.spring_layout(G)

    # Dibujamos nodos y aristas
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=12
    )

    # Obtenemos los pesos
    etiquetas = nx.get_edge_attributes(
        G,
        'weight'
    )

    # Dibujamos los pesos
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=etiquetas
    )

    plt.title("Grafo Utilizado en Dijkstra")

    plt.show()


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # Grafo de ejemplo
    grafo = {

        'A': [('B', 4), ('C', 2)],

        'B': [('A', 4),
              ('C', 1),
              ('D', 5)],

        'C': [('A', 2),
              ('B', 1),
              ('D', 8)],

        'D': [('B', 5),
              ('C', 8)]

    }

    print("\nGRAFO UTILIZADO")

    for nodo in grafo:
        print(nodo, "->", grafo[nodo])

    inicio = input(
        "\nIngrese el nodo inicial (A,B,C,D): "
    ).upper()

    dijkstra_paso_a_paso(
        grafo,
        inicio
    )

    print("\nMostrando gráfica...")

    graficar_grafo(grafo)


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()