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

    # Ordenar usando el algoritmo de burbuja
    bubble_sort(arr, comparisons, swaps, shifts)

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
