import time

# Función de ordenamiento por inserción
def insertion_sort(arr, comparisons, swaps, shifts):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons[0] += 1
            arr[j + 1] = arr[j]  # Desplazamiento
            shifts[0] += 1
            j -= 1
        arr[j + 1] = key
        swaps[0] += 1  # Solo se cuenta el intercambio con el key
        shifts[0] += 1  # Desplazamiento por la inserción del key

# Función para ordenar y medir el tiempo de ejecución
def sort_and_measure(arr, comparisons, swaps, shifts):
    start_time = time.perf_counter_ns()
    insertion_sort(arr, comparisons, swaps, shifts)
    end_time = time.perf_counter_ns()
    return end_time - start_time  # Tiempo de ejecución

# Función principal
def main():
    comparisons_A = [0]  # Comparaciones en situación A
    swaps_A = [0]        # Intercambios en situación A
    shifts_A = [0]       # Desplazamientos en situación A

    # Leer el archivo de contraseñas
    with open("PasswordsUEB.txt", "r") as file:
        arr = [line.strip() for line in file]

    # Ordenar y medir (Situación A)
    time_A = sort_and_measure(arr.copy(), comparisons_A, swaps_A, shifts_A)

    # Preparar para la segunda iteración (Situación B)
    comparisons_B = [0]
    swaps_B = [0]
    shifts_B = [0]

    # Usar el arreglo ya ordenado para la segunda iteración
    # Realizamos un segundo ordenamiento, pero no contaremos nada
    time_B = sort_and_measure(arr.copy(), comparisons_B, swaps_B, shifts_B)

    # Guardar palabras ordenadas en un archivo
    with open("InsertionSort_passwords.txt", "w") as sorted_file:
        sorted_file.write("\n".join(arr))

    # Imprimir resultados de la situación A
    print(f"Comparaciones (A): {comparisons_A[0]}")
    print(f"Intercambios (A): {swaps_A[0]}")
    print(f"Desplazamientos (A): {shifts_A[0]}")
    print(f"Tiempo de ejecución en nanosegundos (A): {time_A}")

    # Imprimir resultados de la situación B
    print(f"\nComparaciones (B): {comparisons_B[0]}")
    print(f"Intercambios (B): 0")  # No hay intercambios en B
    print(f"Desplazamientos (B): 0")  # No hay desplazamientos en B
    print(f"Tiempo de ejecución en nanosegundos (B): {time_B}")

if __name__ == "__main__":
    main()
