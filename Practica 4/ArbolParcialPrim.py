
# SIMULADOR DEL ALGORITMO DE PRIM

# Importamos la biblioteca heapq para manejar una cola
# de prioridad (min-heap).
import heapq

# ----------------------------------------------------------
# Definición del grafo
# Cada nodo contiene una lista de tuplas:
# (nodo vecino, peso de la arista)
# ----------------------------------------------------------
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

# ----------------------------------------------------------
# Función que implementa el algoritmo de Prim
# ----------------------------------------------------------
def prim(grafo, inicio):

    # Conjunto para guardar los nodos visitados
    visitados = set()

    # Lista donde se almacenará el árbol mínimo
    mst = []

    # Costo total del árbol
    costo_total = 0

    # Cola de prioridad
    # (peso, nodo_actual, nodo_destino)
    aristas = []

    # Marcamos el nodo inicial como visitado
    visitados.add(inicio)

    # Agregamos las aristas del nodo inicial
    for vecino, peso in grafo[inicio]:
        heapq.heappush(aristas, (peso, inicio, vecino))

    print("\n========== INICIO DEL ALGORITMO ==========")
    print(f"Nodo inicial: {inicio}")

    paso = 1

    # Mientras existan aristas disponibles
    while aristas:

        # Extraemos la arista de menor peso
        peso, origen, destino = heapq.heappop(aristas)

        print("\n--------------------------------")
        print(f"PASO {paso}")
        print("--------------------------------")
        print(f"Arista seleccionada: {origen} -> {destino}")
        print(f"Peso: {peso}")

        # Si el nodo destino ya fue visitado
        if destino in visitados:
            print("Nodo ya visitado. Se descarta.")
            continue

        # Agregamos el nodo al conjunto de visitados
        visitados.add(destino)

        # Agregamos la arista al MST
        mst.append((origen, destino, peso))

        # Sumamos el costo
        costo_total += peso

        print("Arista agregada al árbol mínimo.")

        print("Nodos visitados:")
        print(visitados)

        print("Costo acumulado:")
        print(costo_total)

        # Agregamos nuevas aristas
        for vecino, peso_vecino in grafo[destino]:

            if vecino not in visitados:
                heapq.heappush(
                    aristas,
                    (peso_vecino, destino, vecino)
                )

        paso += 1

    print("\n===================================")
    print("ÁRBOL PARCIAL MÍNIMO ENCONTRADO")
    print("===================================")

    for origen, destino, peso in mst:
        print(f"{origen} ---- {destino}   Peso={peso}")

    print(f"\nCosto total = {costo_total}")

    return mst, costo_total


# ----------------------------------------------------------
# Programa principal
# ----------------------------------------------------------

mst, costo = prim(grafo, 'A')