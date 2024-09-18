import time

# Función de ordenamiento burbuja
def bubble_sort(arr, comparisons, swaps, shifts):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons[0] += 1
            if arr[j] > arr[j + 1]:  # Orden ascendente
                # Intercambio
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps[0] += 1
                shifts[0] += 2  # Dos desplazamientos por intercambio

def sort_and_measure(arr, comparisons, swaps, shifts):
    start_time = time.perf_counter_ns()
    bubble_sort(arr, comparisons, swaps, shifts)
    end_time = time.perf_counter_ns()
    return end_time - start_time  # Retornar el tiempo de ejecución

def main():
    comparisons_A = [0]  # Comparaciones en situación A
    swaps_A = [0]        # Intercambios en situación A
    shifts_A = [0]       # Desplazamientos en situación A

    comparisons_B = [0]  # Comparaciones en situación B
    swaps_B = [0]        # Intercambios en situación B
    shifts_B = [0]       # Desplazamientos en situación B

    # Leer el archivo de contraseñas
    with open("PasswordsUEB.txt", "r") as file:
        arr = [line.strip() for line in file]

    # Mostrar palabras generadas (Situación A)
    print("Palabras generadas:")
    print(" ".join(arr))

    # Ordenar y medir (Situación A)
    time_A = sort_and_measure(arr, comparisons_A, swaps_A, shifts_A)

    # Mostrar palabras ordenadas (Situación A)
    print("\nPalabras ordenadas (Situación A):")
    print(" ".join(arr))

    # Volver a ordenar (Situación B)
    time_B = sort_and_measure(arr, comparisons_B, swaps_B, shifts_B)

    # Mostrar palabras ordenadas (Situación B)
    print("\nPalabras ordenadas nuevamente (Situación B):")
    print(" ".join(arr))

    # Mostrar resultados de la situación A
    print(f"\nComparaciones (A): {comparisons_A[0]}")
    print(f"Intercambios (A): {swaps_A[0]}")
    print(f"Desplazamientos (A): {shifts_A[0]}")
    print(f"Tiempo de ejecución en nanosegundos (A): {time_A}")

    # Mostrar resultados de la situación B
    print(f"\nComparaciones (B): {comparisons_B[0]}")
    print(f"Intercambios (B): {swaps_B[0]}")
    print(f"Desplazamientos (B): {shifts_B[0]}")
    print(f"Tiempo de ejecución en nanosegundos (B): {time_B}")

if __name__ == "__main__":
    main()
