# Función para fusionar dos listas ordenadas
def fusionar(izquierda, derecha):

    # Lista resultado
    resultado = []

    # Índices de recorrido
    i = 0
    j = 0

    # Comparar elementos
    while i < len(izquierda) and j < len(derecha):

        # Si el elemento izquierdo es menor
        if izquierda[i] <= derecha[j]:

            # Agregar a resultado
            resultado.append(izquierda[i])

            # Avanzar índice
            i += 1

        else:

            # Agregar elemento derecho
            resultado.append(derecha[j])

            # Avanzar índice
            j += 1

    # Agregar elementos sobrantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    # Retornar lista fusionada
    return resultado


# Detecta secuencias ordenadas naturales
def obtener_runs(lista):

    # Lista donde se guardarán las secuencias
    runs = []

    # Primera secuencia
    run_actual = [lista[0]]

    # Recorrer desde el segundo elemento
    for i in range(1, len(lista)):

        # Si mantiene el orden ascendente
        if lista[i] >= lista[i - 1]:

            # Agregar al run actual
            run_actual.append(lista[i])

        else:

            # Guardar run terminado
            runs.append(run_actual)

            # Crear nuevo run
            run_actual = [lista[i]]

    # Guardar último run
    runs.append(run_actual)

    # Retornar runs encontrados
    return runs


# Función Natural Merging
def natural_merging(lista):

    # Repetir hasta tener una sola secuencia
    while True:

        # Obtener secuencias naturales
        runs = obtener_runs(lista)

        # Si solo existe una, ya está ordenada
        if len(runs) == 1:
            return runs[0]

        # Lista para nuevos runs fusionados
        nuevos_runs = []

        # Fusionar pares de runs
        for i in range(0, len(runs), 2):

            # Si existe pareja
            if i + 1 < len(runs):

                # Fusionar ambos runs
                nuevos_runs.append(
                    fusionar(runs[i], runs[i + 1])
                )

            else:

                # Si queda uno solo, conservarlo
                nuevos_runs.append(runs[i])

        # Reconstruir lista
        lista = []

        # Unir todos los runs
        for run in nuevos_runs:
            lista.extend(run)


# Ejemplo de uso
numeros = [5, 8, 12, 2, 7, 9, 1, 4, 6]

# Ordenar
resultado = natural_merging(numeros)

# Mostrar resultado
print("Lista ordenada:", resultado)