# Función que implementa el algoritmo Insertion Sort
def insertion_sort(lista):

    # Recorre la lista desde el segundo elemento
    for i in range(1, len(lista)):

        # Guarda el valor actual que se desea insertar
        clave = lista[i]

        # Variable auxiliar para comparar elementos anteriores
        j = i - 1

        # Mientras existan elementos mayores que la clave
        # se desplazan una posición hacia la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1

        # Inserta la clave en su posición correcta
        lista[j + 1] = clave

    # Retorna la lista ordenada
    return lista


# Ejemplo de uso
datos = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", datos)

resultado = insertion_sort(datos)

print("Lista ordenada:", resultado)