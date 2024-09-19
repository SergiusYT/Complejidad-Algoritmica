import time
import sys

# Aumentar el límite de recursión si es necesario
sys.setrecursionlimit(3000)

# Función de partición con pivote en el medio
def partition(arr, low, high, comparisons, swaps, shifts):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]  # Mover el pivote al final
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

# Función QuickSort con pivote mejorado
def quick_sort(arr, low, high, comparisons, swaps, shifts):
    while low < high:
        pi = partition(arr, low, high, comparisons, swaps, shifts)

        # Elegir la parte más pequeña para evitar una pila profunda
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1, comparisons, swaps, shifts)
            low = pi + 1  # Evitar recursión profunda
        else:
            quick_sort(arr, pi + 1, high, comparisons, swaps, shifts)
            high = pi - 1

# Función para ordenar y medir el tiempo de ejecución
def sort_and_measure(arr, comparisons, swaps, shifts):
    start_time = time.perf_counter_ns()
    quick_sort(arr, 0, len(arr) - 1, comparisons, swaps, shifts)
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

    # Ordenar y medir (Situación A)
    time_A = sort_and_measure(arr, comparisons_A, swaps_A, shifts_A)

    # Volver a ordenar (Situación B)
    time_B = sort_and_measure(arr, comparisons_B, swaps_B, shifts_B)

    # Guardar palabras ordenadas en un archivo
    with open("QuickSort_passwords.txt", "w") as sorted_file:
        sorted_file.write("\n".join(arr))

    # Imprimir resultados de la situación A
    print(f"Comparaciones (A): {comparisons_A[0]}")
    print(f"Intercambios (A): {swaps_A[0]}")
    print(f"Desplazamientos (A): {shifts_A[0]}")
    print(f"Tiempo de ejecución en nanosegundos (A): {time_A}")

    # Imprimir resultados de la situación B
    print(f"\nComparaciones (B): {comparisons_B[0]}")
    print(f"Intercambios (B): {swaps_B[0]}")
    print(f"Desplazamientos (B): {shifts_B[0]}")
    print(f"Tiempo de ejecución en nanosegundos (B): {time_B}")

if __name__ == "__main__":
    main()
