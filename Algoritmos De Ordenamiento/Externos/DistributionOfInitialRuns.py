# Función para generar runs iniciales
def generar_runs(lista, tamaño_run):

    # Lista que almacenará los runs
    runs = []

    # Recorrer la lista por bloques
    for i in range(0, len(lista), tamaño_run):

        # Extraer bloque
        bloque = lista[i:i + tamaño_run]

        # Ordenar bloque
        bloque.sort()

        # Guardar run
        runs.append(bloque)

    # Retornar runs
    return runs


# Datos originales
datos = [25, 12, 40, 8, 19, 3, 15, 50]

# Crear runs de tamaño 3
runs = generar_runs(datos, 3)

# Mostrar resultado
print("Runs iniciales:")

for run in runs:
    print(run)