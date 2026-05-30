# Función principal de QuickSort
def quicksort(lista):
    
    # Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Se selecciona el elemento central como pivote
    pivote = lista[len(lista) // 2]

    # Se crean tres listas:
    # menores: elementos menores que el pivote
    menores = [x for x in lista if x < pivote]

    # iguales: elementos iguales al pivote
    iguales = [x for x in lista if x == pivote]

    # mayores: elementos mayores que el pivote
    mayores = [x for x in lista if x > pivote]

    # Se ordenan recursivamente menores y mayores
    # Luego se concatenan los resultados
    return quicksort(menores) + iguales + quicksort(mayores)


# Lista de ejemplo
numeros = [34, 7, 23, 32, 5, 62]

# Se llama al algoritmo
resultado = quicksort(numeros)

# Se imprime la lista ordenada
print("Lista ordenada:", resultado)