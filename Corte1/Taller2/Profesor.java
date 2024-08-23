import java.util.Scanner;

public class Profesor {  
    public static void main(String[] args) {
        long inicio = System.nanoTime();

        Scanner entrada = new Scanner(System.in);
        System.out.print("Valor de -n-: ");
        int n = entrada.nextInt();

        for (int exp = 0; exp <= n; exp++) {
            System.out.println("2 Elevado a " + exp + " igual a " + (1 << exp));
        }

        entrada.close();

        
        long finalizacion = System.nanoTime();

        
        long duracion = finalizacion - inicio;
        System.out.println("\nEl algoritmo se ejecutó en: " + duracion + " nanosegundos");
    }
}
