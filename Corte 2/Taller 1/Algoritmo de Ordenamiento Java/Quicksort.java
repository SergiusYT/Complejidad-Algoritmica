import java.util.Random;

public class Quicksort {
    static final int N = 1000;

    public static int partition(int[] arr, int low, int high, int[] comparisons, int[] swaps) {
        int pivot = arr[high];
        int i = low - 1;
        int temp;

        for (int j = low; j <= high - 1; j++) {
            comparisons[0]++;
            if (arr[j] > pivot) {
                i++;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                swaps[0]++;
            }
        }
        temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        swaps[0]++;
        return i + 1;
    }

    public static void quickSort(int[] arr, int low, int high, int[] comparisons, int[] swaps) {
        if (low < high) {
            int pi = partition(arr, low, high, comparisons, swaps);

            quickSort(arr, low, pi - 1, comparisons, swaps);
            quickSort(arr, pi + 1, high, comparisons, swaps);
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

        quickSort(arr, 0, N - 1, comparisons, swaps);

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

