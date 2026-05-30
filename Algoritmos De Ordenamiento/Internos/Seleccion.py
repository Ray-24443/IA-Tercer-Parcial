# Función que implementa el algoritmo Selection Sort
def selection_sort(lista):

    # Recorre toda la lista
    for i in range(len(lista)):

        # Supone que el elemento actual es el mínimo
        indice_minimo = i

        # Busca el elemento más pequeño en el resto de la lista
        for j in range(i + 1, len(lista)):

            # Si encuentra un valor menor
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambia el mínimo encontrado con la posición actual
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    # Retorna la lista ordenada
    return lista


# Ejemplo de uso
datos = [29, 10, 14, 37, 13]

print("Lista original:", datos)

resultado = selection_sort(datos)

print("Lista ordenada:", resultado)