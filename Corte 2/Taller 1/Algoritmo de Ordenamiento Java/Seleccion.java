import java.util.Random;

public class Seleccion {
    public static final int N = 1000;

    public static void selectionSort(int[] arr, int n, int[] comparisons, int[] swaps) {
        int min_idx, temp;
        for (int i = 0; i < n - 1; i++) {
            min_idx = i;
            for (int j = i + 1; j < n; j++) {
                comparisons[0]++;
                if (arr[j] > arr[min_idx]) {
                    min_idx = j;
                }
            }

            // Swap
            if (min_idx != i) {
                temp = arr[i];
                arr[i] = arr[min_idx];
                arr[min_idx] = temp;
                swaps[0]++;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[N];
        int[] comparisons = {0};
        int[] swaps = {0};

        Random rand = new Random();
        // Medir el tiempo de ejecución
        long startTime = System.nanoTime();
        for (int i = 0; i < N; i++) {
            arr[i] = rand.nextInt(302501 - 300000) + 300000;
        }

        System.out.println("Numeros generados:");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n");

        selectionSort(arr, N, comparisons, swaps);

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("Numeros ordenados:");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n\n");

        System.out.println("Comparaciones: " + comparisons[0]);
        System.out.println("Intercambios: " + swaps[0]);
        System.out.println("Estable: No");
        System.out.println("Insercion: No");
        // Mostrar el tiempo de ejecución en nanosegundos
        System.out.println("Tiempo de ejecucion en nanosegundos: " + duration);
    }
}
