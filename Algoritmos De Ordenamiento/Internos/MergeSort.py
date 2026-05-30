# Función MergeSort
def mergesort(lista):

    # Caso base: una lista de tamaño 0 o 1 ya está ordenada
    if len(lista) <= 1:
        return lista

    # Se calcula el punto medio de la lista
    mitad = len(lista) // 2

    # Se divide la lista en dos partes
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Se ordenan ambas mitades de forma recursiva
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    # Se mezclan las dos listas ordenadas
    return fusionar(izquierda, derecha)


# Función para fusionar dos listas ordenadas
def fusionar(izquierda, derecha):

    # Lista donde se guardará el resultado
    resultado = []

    # Índice para recorrer la lista izquierda
    i = 0

    # Índice para recorrer la lista derecha
    j = 0

    # Mientras existan elementos en ambas listas
    while i < len(izquierda) and j < len(derecha):

        # Si el elemento de la izquierda es menor
        if izquierda[i] < derecha[j]:

            # Se agrega al resultado
            resultado.append(izquierda[i])

            # Se avanza al siguiente elemento
            i += 1

        else:
            # Se agrega el elemento de la derecha
            resultado.append(derecha[j])

            # Se avanza al siguiente elemento
            j += 1

    # Se agregan los elementos restantes de la izquierda
    resultado.extend(izquierda[i:])

    # Se agregan los elementos restantes de la derecha
    resultado.extend(derecha[j:])

    # Se devuelve la lista fusionada
    return resultado


# Lista de prueba
numeros = [34, 7, 23, 32, 5, 62]

# Ordenamiento
resultado = mergesort(numeros)

# Mostrar resultado
print("Lista ordenada:", resultado)