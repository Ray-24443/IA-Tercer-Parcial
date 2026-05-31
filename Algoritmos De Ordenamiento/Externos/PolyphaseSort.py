# Función que genera números de Fibonacci
def fibonacci(n):

    # Primeros dos números
    fib = [1, 1]

    # Generar la secuencia
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    # Retornar secuencia
    return fib


# Simulación de distribución Polyphase
def polyphase_sort(runs):

    # Obtener cantidad de runs
    cantidad = len(runs)

    # Generar secuencia Fibonacci
    fib = fibonacci(cantidad + 2)

    # Mostrar distribución teórica
    print("Distribución Fibonacci:")

    # Imprimir valores
    for valor in fib:
        print(valor, end=" ")

    print()

    # Simulación de mezcla final
    resultado = []

    # Recorrer todos los runs
    for run in runs:

        # Agregar elementos
        resultado.extend(run)

    # Ordenar resultado
    resultado.sort()

    # Retornar resultado
    return resultado


# Runs de ejemplo
runs = [
    [2, 8],
    [1, 5],
    [4, 7]
]

# Ejecutar simulación
resultado = polyphase_sort(runs)

# Mostrar resultado
print("Resultado:", resultado)