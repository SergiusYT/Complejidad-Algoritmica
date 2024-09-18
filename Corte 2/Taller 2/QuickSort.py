import time

# Función de partición
def partition(arr, low, high, comparisons, swaps, shifts):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] < pivot:  # Orden ascendente
            i += 1
            # Intercambiar elementos
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1
            shifts[0] += 2  # Dos desplazamientos por intercambio

    # Intercambiar el pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps[0] += 1
    shifts[0] += 2  # Dos desplazamientos por intercambio
    return i + 1

# Función QuickSort
def quick_sort(arr, low, high, comparisons, swaps, shifts):
    if low < high:
        pi = partition(arr, low, high, comparisons, swaps, shifts)
        quick_sort(arr, low, pi - 1, comparisons, swaps, shifts)
        quick_sort(arr, pi + 1, high, comparisons, swaps, shifts)

def main():
    comparisons = [0]  # Comparaciones
    swaps = [0]        # Intercambios
    shifts = [0]       # Desplazamientos

    # Leer el archivo de contraseñas
    with open("PasswordsUEB.txt", "r") as file:
        arr = [line.strip() for line in file]

    # Mostrar palabras generadas
    print("Palabras generadas:")
    print(" ".join(arr))

    # Medir el tiempo de ejecución
    start_time = time.perf_counter_ns()

    # Ordenar usando el algoritmo QuickSort
    quick_sort(arr, 0, len(arr) - 1, comparisons, swaps, shifts)

    end_time = time.perf_counter_ns()

    # Calcular el tiempo transcurrido en nanosegundos
    time_taken = end_time - start_time

    # Mostrar palabras ordenadas
    print("\nPalabras ordenadas:")
    print(" ".join(arr))

    # Mostrar resultados
    print(f"\nComparaciones: {comparisons[0]}")
    print(f"Intercambios: {swaps[0]}")
    print(f"Desplazamientos: {shifts[0]}")
    print(f"Tiempo de ejecución en nanosegundos: {time_taken}")

if __name__ == "__main__":
    main()
