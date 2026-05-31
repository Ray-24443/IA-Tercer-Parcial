# Importar heapq para utilizar una cola de prioridad (min-heap)
import heapq

# Función para realizar la mezcla multicamino
def balanced_multiway_merge(runs):

    # Crear un heap vacío
    heap = []

    # Lista donde se almacenará el resultado final
    resultado = []

    # Insertar el primer elemento de cada run en el heap
    for i in range(len(runs)):

        # Verificar que el run no esté vacío
        if len(runs[i]) > 0:

            # Guardar:
            # valor, índice del run, posición dentro del run
            heapq.heappush(heap, (runs[i][0], i, 0))

    # Mientras existan elementos en el heap
    while heap:

        # Extraer el menor elemento
        valor, run_actual, posicion = heapq.heappop(heap)

        # Agregar al resultado
        resultado.append(valor)

        # Calcular siguiente posición del mismo run
        siguiente = posicion + 1

        # Verificar si existe otro elemento
        if siguiente < len(runs[run_actual]):

            # Insertarlo en el heap
            heapq.heappush(
                heap,
                (
                    runs[run_actual][siguiente],
                    run_actual,
                    siguiente
                )
            )

    # Retornar lista fusionada
    return resultado


# Runs ordenados
runs = [
    [1, 8, 15],
    [2, 6, 20],
    [4, 9, 30]
]

# Ejecutar algoritmo
resultado = balanced_multiway_merge(runs)

# Mostrar resultado
print("Resultado:", resultado)