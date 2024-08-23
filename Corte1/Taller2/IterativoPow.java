import java.util.Scanner;

public class IterativoPow {
    public static void main(String[] args) {
        long inicio = System.nanoTime();

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un número entero positivo <= 20: ");
        int n = scanner.nextInt();

        if (n <= 0 || n > 20) {
            System.out.println("Error: El número debe ser entero positivo y menor o igual a 20.");
			
            long finalizacion = System.nanoTime();
            
            long duracion = finalizacion - inicio;
            System.out.println("\nEl algoritmo se ejecutó en: " + duracion + " nanosegundos");
			scanner.close();
            return;
        }

        for (int i = 0; i <= n; i++) {
            int resultado = (int) Math.pow(2, i);
            System.out.println("2 ^ " + i + " = " + resultado);
        }

        scanner.close();

        long finalizacion = System.nanoTime();

        long duracion = finalizacion - inicio;
        System.out.println("\nEl algoritmo se ejecutó en: " + duracion + " nanosegundos");
    }
}
