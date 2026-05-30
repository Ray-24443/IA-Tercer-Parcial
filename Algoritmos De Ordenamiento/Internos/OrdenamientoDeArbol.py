# Clase que representa un nodo del árbol
class Nodo:

    # Constructor de la clase
    def __init__(self, valor):

        # Valor almacenado en el nodo
        self.valor = valor

        # Referencia al hijo izquierdo
        self.izquierda = None

        # Referencia al hijo derecho
        self.derecha = None


# Función para insertar elementos en el árbol
def insertar(raiz, valor):

    # Si el valor es menor, se inserta a la izquierda
    if valor < raiz.valor:

        # Si no existe hijo izquierdo
        if raiz.izquierda is None:
            raiz.izquierda = Nodo(valor)

        else:
            insertar(raiz.izquierda, valor)

    # Si el valor es mayor o igual, va a la derecha
    else:

        # Si no existe hijo derecho
        if raiz.derecha is None:
            raiz.derecha = Nodo(valor)

        else:
            insertar(raiz.derecha, valor)


# Recorrido InOrder para obtener datos ordenados
def inorder(raiz, resultado):

    # Verifica que exista nodo
    if raiz:

        # Recorre el subárbol izquierdo
        inorder(raiz.izquierda, resultado)

        # Agrega el valor actual
        resultado.append(raiz.valor)

        # Recorre el subárbol derecho
        inorder(raiz.derecha, resultado)


# Función principal Tree Sort
def tree_sort(lista):

    # Si la lista está vacía
    if len(lista) == 0:
        return []

    # Crea la raíz con el primer elemento
    raiz = Nodo(lista[0])

    # Inserta los elementos restantes
    for valor in lista[1:]:
        insertar(raiz, valor)

    # Lista donde se almacenará el resultado
    resultado = []

    # Obtiene los elementos ordenados
    inorder(raiz, resultado)

    # Retorna la lista ordenada
    return resultado


# Ejemplo de uso
datos = [7, 4, 9, 1, 6, 8, 10]

print("Lista original:", datos)

resultado = tree_sort(datos)

print("Lista ordenada:", resultado)