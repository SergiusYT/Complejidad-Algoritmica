import java.util.Random;

public class Insercion {
    
    public static void insertionSort(int[] arr, int n, int[] comparisons, int[] swaps) {
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] < key) {
                comparisons[0]++;
                arr[j + 1] = arr[j];
                j = j - 1;
                swaps[0]++;
            }
            arr[j + 1] = key;
            swaps[0]++;
        }
    }

    public static void main(String[] args) {
        final int N = 1000;
        int[] arr = new int[N];
        int[] comparisons = {0};
        int[] swaps = {0};

        Random rand = new Random();
        // Medir el tiempo de ejecución
        long startTime = System.nanoTime();
        for (int i = 0; i < N; i++) {
            arr[i] = rand.nextInt(302501 - 300000) + 300000;
        }

        System.out.println("Números generados:");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n");

        insertionSort(arr, N, comparisons, swaps);

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("Numeros ordenados:");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n\n");

        System.out.println("Comparaciones: " + comparisons[0]);
        System.out.println("Intercambios: " + swaps[0]);
        System.out.println("Estable: Si");
        System.out.println("Insercion: Si");

        // Mostrar el tiempo de ejecución en nanosegundos
        System.out.println("Tiempo de ejecucion en nanosegundos: " + duration);
    }
}
