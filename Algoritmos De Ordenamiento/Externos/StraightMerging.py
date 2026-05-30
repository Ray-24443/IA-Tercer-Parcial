# Función para fusionar dos sublistas ordenadas
def fusionar(izquierda, derecha):

    # Lista donde se almacenará el resultado
    resultado = []

    # Índice para recorrer la sublista izquierda
    i = 0

    # Índice para recorrer la sublista derecha
    j = 0

    # Comparar elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):

        # Si el elemento izquierdo es menor o igual
        if izquierda[i] <= derecha[j]:

            # Agregarlo al resultado
            resultado.append(izquierda[i])

            # Avanzar índice izquierdo
            i += 1

        else:

            # Agregar elemento derecho
            resultado.append(derecha[j])

            # Avanzar índice derecho
            j += 1

    # Agregar elementos restantes de la izquierda
    resultado.extend(izquierda[i:])

    # Agregar elementos restantes de la derecha
    resultado.extend(derecha[j:])

    # Retornar lista fusionada
    return resultado


# Función Straight Merging
def straight_merging(lista):

    # Tamaño inicial de los bloques
    tamaño = 1

    # Número total de elementos
    n = len(lista)

    # Mientras el tamaño del bloque sea menor que la lista
    while tamaño < n:

        # Lista temporal para guardar el resultado
        nueva_lista = []

        # Recorrer la lista por bloques
        for i in range(0, n, 2 * tamaño):

            # Primer bloque
            izquierda = lista[i:i + tamaño]

            # Segundo bloque
            derecha = lista[i + tamaño:i + 2 * tamaño]

            # Fusionar ambos bloques
            nueva_lista.extend(fusionar(izquierda, derecha))

        # Actualizar lista
        lista = nueva_lista

        # Duplicar tamaño del bloque
        tamaño *= 2

    # Retornar lista ordenada
    return lista


# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]

# Ordenar
resultado = straight_merging(numeros)

# Mostrar resultado
print("Lista ordenada:", resultado)