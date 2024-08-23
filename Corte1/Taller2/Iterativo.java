import java.util.Scanner;

public class Iterativo {
    public static void main(String[] args) {
        long inicio = System.nanoTime();

        Scanner scanner = new Scanner(System.in); 
        System.out.print("Ingresa el exponente máximo entero positivo: ");
        int exponente = scanner.nextInt();
        int base = 2;
        long resultado = 1;

        for (int i = 1; i <= exponente; i++) {
            resultado *= base;
            System.out.println(base + "^" + i + " = " + resultado);            
        }
        
        scanner.close();
        
        long finalizacion = System.nanoTime();

        long duracion = finalizacion - inicio;
        System.out.println("\nEl algoritmo se ejecutó en: " + duracion + " nanosegundos");
    }
}
