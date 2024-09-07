import random
import time

# Función de ordenamiento por inserción
def insertion_sort(arr, comparisons, swaps):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Comparar e insertar
        while j >= 0 and arr[j] > key:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps[0] += 1
        arr[j + 1] = key
        swaps[0] += 1

def main():
    N = 1000
    arr = [0] * N
    comparisons = [0]  # Usamos una lista para permitir la modificación dentro de la función
    swaps = [0]

    # Medir el tiempo de ejecución
    start_time = time.perf_counter_ns()

    # Generar números aleatorios de 0 a 9
    for i in range(N):
        arr[i] = random.randint(0, 9)  # Números entre 0 y 9

    # Mostrar números generados
    print("Números generados:")
    print(" ".join(map(str, arr)))

    # Ordenar usando el algoritmo de inserción
    insertion_sort(arr, comparisons, swaps)

    end_time = time.perf_counter_ns()

    # Calcular el tiempo transcurrido en nanosegundos
    time_taken = end_time - start_time

    # Mostrar números ordenados
    print("\nNúmeros ordenados:")
    print(" ".join(map(str, arr)))

    # Mostrar resultados
    print(f"\nComparaciones: {comparisons[0]}")
    print(f"Intercambios: {swaps[0]}")
    print("Estable: Sí")
    print("Inserción: Sí")

    # Mostrar el tiempo de ejecución en nanosegundos
    print(f"Tiempo de ejecución en nanosegundos: {time_taken}")

if __name__ == "__main__":
    main()
