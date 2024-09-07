#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000

void selectionSort(int arr[], int n, int *comparisons, int *swaps) {
    int i, j, min_idx, temp;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            (*comparisons)++;
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        // Swap
        if (min_idx != i) {
            temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
            (*swaps)++;
        }
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

    // Ordenar usando el algoritmo de selección
    selectionSort(arr, N, &comparisons, &swaps);

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
