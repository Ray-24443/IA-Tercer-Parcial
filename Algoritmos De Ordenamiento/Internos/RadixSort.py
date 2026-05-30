# Función RadixSort
def radix_sort(lista):

    # Se obtiene el número más grande de la lista
    maximo = max(lista)

    # Variable que representa la posición decimal
    exp = 1

    # Se repite mientras existan dígitos por procesar
    while maximo // exp > 0:

        # Se ordena según el dígito actual
        counting_sort(lista, exp)

        # Se pasa a la siguiente posición decimal
        exp *= 10

    # Se devuelve la lista ordenada
    return lista


# Counting Sort utilizado por Radix Sort
def counting_sort(lista, exp):

    # Cantidad de elementos
    n = len(lista)

    # Lista temporal para almacenar resultados
    salida = [0] * n

    # Arreglo de conteo para los dígitos 0-9
    conteo = [0] * 10

    # Contar ocurrencias de cada dígito
    for numero in lista:

        # Obtener el dígito correspondiente
        indice = (numero // exp) % 10

        # Incrementar contador
        conteo[indice] += 1

    # Convertir conteos en posiciones acumuladas
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la salida recorriendo de derecha a izquierda
    for i in range(n - 1, -1, -1):

        # Obtener el dígito actual
        indice = (lista[i] // exp) % 10

        # Colocar el elemento en su posición correcta
        salida[conteo[indice] - 1] = lista[i]

        # Reducir el contador
        conteo[indice] -= 1

    # Copiar los datos ordenados a la lista original
    for i in range(n):
        lista[i] = salida[i]


# Lista de prueba
numeros = [170, 45, 75, 90, 802, 24, 2, 66]

# Ejecutar algoritmo
resultado = radix_sort(numeros)

# Mostrar resultado
print("Lista ordenada:", resultado)