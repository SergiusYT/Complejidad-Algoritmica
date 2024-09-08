import java.util.Random;

public class Burbuja {

    public static void bubbleSort(int[] arr, int n, int[] comparisons, int[] swaps) {
        int temp;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                comparisons[0]++;
                if (arr[j] < arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swaps[0]++;
                }
            }
        }
    }

    public static void main(String[] args) {
        int N = 1000;
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

        bubbleSort(arr, N, comparisons, swaps);

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
        System.out.println("Insercion: No");



        // Mostrar el tiempo de ejecución en nanosegundos
        System.out.println("Tiempo de ejecucion en nanosegundos: " + duration);
    }

    
}
