# ============================================================
# ALGORITMO DE KRUSKAL
# Árbol de Mínimo y Máximo Coste
# Simulación paso a paso
# ============================================================

# ------------------------------------------------------------
# Clase Union-Find (Disjoint Set)
# Se utiliza para detectar ciclos
# ------------------------------------------------------------

class UnionFind:

    # Constructor
    def __init__(self, vertices):

        # Cada nodo inicia siendo su propio padre
        self.padre = {}

        for v in vertices:
            self.padre[v] = v

    # Buscar la raíz
    def encontrar(self, nodo):

        if self.padre[nodo] == nodo:
            return nodo

        return self.encontrar(self.padre[nodo])

    # Unir conjuntos
    def unir(self, nodo1, nodo2):

        raiz1 = self.encontrar(nodo1)
        raiz2 = self.encontrar(nodo2)

        self.padre[raiz2] = raiz1


# ------------------------------------------------------------
# Función Kruskal
# minimo=True  -> Árbol de mínimo coste
# minimo=False -> Árbol de máximo coste
# ------------------------------------------------------------

def kruskal(vertices, aristas, minimo=True):

    print("\n========================================")
    if minimo:
        print(" KRUSKAL - ARBOL DE MINIMO COSTE")
    else:
        print(" KRUSKAL - ARBOL DE MAXIMO COSTE")
    print("========================================")

    # Ordenar aristas
    aristas_ordenadas = sorted(
        aristas,
        key=lambda x: x[2],
        reverse=not minimo
    )

    print("\nAristas ordenadas:")

    for origen, destino, peso in aristas_ordenadas:
        print(f"{origen} - {destino} = {peso}")

    uf = UnionFind(vertices)

    mst = []

    costo_total = 0

    paso = 1

    print("\nProceso:\n")

    for origen, destino, peso in aristas_ordenadas:

        print("-----------------------------------")
        print(f"PASO {paso}")
        print("-----------------------------------")

        print(
            f"Evaluando arista "
            f"{origen} - {destino}"
            f" (peso={peso})"
        )

        raiz1 = uf.encontrar(origen)
        raiz2 = uf.encontrar(destino)

        # Si son diferentes no forman ciclo
        if raiz1 != raiz2:

            print("No forma ciclo")

            uf.unir(origen, destino)

            mst.append((origen, destino, peso))

            costo_total += peso

            print("Arista agregada")

        else:

            print("Forma ciclo")
            print("Arista descartada")

        paso += 1

    print("\n================================")
    print("RESULTADO")
    print("================================")

    for origen, destino, peso in mst:
        print(
            f"{origen} --- {destino}"
            f"   peso={peso}"
        )

    print(f"\nCosto total = {costo_total}")

    return mst


# ------------------------------------------------------------
# Grafo de ejemplo
# ------------------------------------------------------------

vertices = ['A', 'B', 'C', 'D', 'E', 'F']

aristas = [

    ('A', 'B', 4),
    ('A', 'C', 2),

    ('B', 'C', 1),
    ('B', 'D', 5),

    ('C', 'D', 8),
    ('C', 'E', 10),

    ('D', 'E', 2),
    ('D', 'F', 6),

    ('E', 'F', 3)

]

# ------------------------------------------------------------
# Ejecutar mínimo coste
# ------------------------------------------------------------

mst_minimo = kruskal(
    vertices,
    aristas,
    True
)

# ------------------------------------------------------------
# Ejecutar máximo coste
# ------------------------------------------------------------

mst_maximo = kruskal(
    vertices,
    aristas,
    False
)

#Parte Grafica
import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------------------
# Crear grafo completo
# ------------------------------------------

G = nx.Graph()

for origen, destino, peso in aristas:
    G.add_edge(
        origen,
        destino,
        weight=peso
    )

# Posición fija
pos = nx.spring_layout(
    G,
    seed=42
)

# ------------------------------------------
# Graficar
# ------------------------------------------

plt.figure(figsize=(10,7))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500
)

# Pesos
etiquetas = nx.get_edge_attributes(
    G,
    'weight'
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=etiquetas
)

# Árbol mínimo resaltado
MST = nx.Graph()

for origen, destino, peso in mst_minimo:

    MST.add_edge(
        origen,
        destino
    )

nx.draw_networkx_edges(
    MST,
    pos,
    width=5
)

plt.title(
    "Arbol de Minimo Coste - Kruskal"
)

plt.show()