# Función que implementa el algoritmo Bubble Sort
def intercambio(lista):

    # Obtiene la cantidad de elementos
    n = len(lista)

    # Realiza n recorridos
    for i in range(n):

        # Recorre la parte no ordenada de la lista
        for j in range(0, n - i - 1):

            # Compara elementos consecutivos
            if lista[j] > lista[j + 1]:

                # Intercambia los elementos si están en orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Retorna la lista ordenada
    return lista


# Ejemplo de uso
datos = [5, 1, 4, 2, 8]

print("Lista original:", datos)

resultado = intercambio(datos)

print("Lista ordenada:", resultado)