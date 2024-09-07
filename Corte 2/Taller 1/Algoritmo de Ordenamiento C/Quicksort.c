#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000

int partition(int arr[], int low, int high, int *comparisons, int *swaps) {
    int pivot = arr[high];
    int i = (low - 1);
    int temp;

    for (int j = low; j <= high - 1; j++) {
        (*comparisons)++;
        if (arr[j] < pivot) {
            i++;
            // Swap
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            (*swaps)++;
        }
    }
    // Swap pivot
    temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    (*swaps)++;
    return (i + 1);
}

void quickSort(int arr[], int low, int high, int *comparisons, int *swaps) {
    if (low < high) {
        int pi = partition(arr, low, high, comparisons, swaps);

        quickSort(arr, low, pi - 1, comparisons, swaps);
        quickSort(arr, pi + 1, high, comparisons, swaps);
    }
}

int main() {
    int arr[N];
    int comparisons = 0, swaps = 0;

    // Medir el tiempo de ejecución
    clock_t start, end;
    start = clock();

    // Generar números aleatorios de 0 a 9
    srand(time(0));
    for (int i = 0; i < N; i++) {
        arr[i] = rand() % 10; // Números entre 0 y 9
    }

    // Mostrar números generados
    printf("Numeros generados:\n");
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Ordenar usando el algoritmo QuickSort
    quickSort(arr, 0, N - 1, &comparisons, &swaps);

    end = clock();

    // Calcular el tiempo transcurrido en nanosegundos
    double time_taken = ((double)(end - start) / CLOCKS_PER_SEC) * 1000000000;

    // Mostrar números ordenados
    printf("Numeros ordenados:\n");
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Mostrar resultados
    printf("Comparaciones: %d\n", comparisons);
    printf("Intercambios: %d\n", swaps);
    printf("Estable: No\n");
    printf("Insercion: No\n");
    // Mostrar el tiempo de ejecución en nanosegundos
    printf("Tiempo de ejecucion en nanosegundos: %.0f\n", time_taken);

    return 0;
}
