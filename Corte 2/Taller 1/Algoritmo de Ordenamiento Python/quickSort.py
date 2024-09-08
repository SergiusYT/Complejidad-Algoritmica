import random
import time

# Función de partición
def partition(arr, low, high, comparisons, swaps):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] > pivot:
            i += 1
            # Intercambiar elementos
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1

    # Intercambiar el pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps[0] += 1
    return i + 1

# Función QuickSort
def quick_sort(arr, low, high, comparisons, swaps):
    if low < high:
        pi = partition(arr, low, high, comparisons, swaps)
        quick_sort(arr, low, pi - 1, comparisons, swaps)
        quick_sort(arr, pi + 1, high, comparisons, swaps)

def main():
    N = 1000
    arr = [0] * N
    comparisons = [0]  # Usamos una lista para permitir modificaciones dentro de las funciones
    swaps = [0]

    # Medir el tiempo de ejecución
    start_time = time.perf_counter_ns()

    # Generar números aleatorios de 0 a 9
    for i in range(N):
        arr[i] = random.randint(300000,302500)  # Números entre 300000 y 302500

    # Mostrar números generados
    print("Números generados:")
    print(" ".join(map(str, arr)))

    # Ordenar usando el algoritmo QuickSort
    quick_sort(arr, 0, N - 1, comparisons, swaps)

    end_time = time.perf_counter_ns()

    # Calcular el tiempo transcurrido en nanosegundos
    time_taken = end_time - start_time

    # Mostrar números ordenados
    print("\nNúmeros ordenados:")
    print(" ".join(map(str, arr)))

    # Mostrar resultados
    print(f"\nComparaciones: {comparisons[0]}")
    print(f"Intercambios: {swaps[0]}")
    print("Estable: No")
    print("Inserción: No")

    # Mostrar el tiempo de ejecución en nanosegundos
    print(f"Tiempo de ejecución en nanosegundos: {time_taken}")

if __name__ == "__main__":
    main()
