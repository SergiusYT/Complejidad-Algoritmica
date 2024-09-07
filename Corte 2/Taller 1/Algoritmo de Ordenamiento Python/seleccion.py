import random
import time

# Función Selection Sort
def selection_sort(arr, n, comparisons, swaps):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons[0] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambio
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps[0] += 1

def main():
    N = 1000
    arr = [0] * N
    comparisons = [0]  # Usamos una lista para poder modificar el valor dentro de las funciones
    swaps = [0]

    # Medir el tiempo de ejecución
    start_time = time.perf_counter_ns()

    # Generar números aleatorios de 0 a 9
    for i in range(N):
        arr[i] = random.randint(0, 9)

    # Mostrar números generados
    print("Números generados:")
    print(" ".join(map(str, arr)))

    # Ordenar usando el algoritmo de selección
    selection_sort(arr, N, comparisons, swaps)

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
