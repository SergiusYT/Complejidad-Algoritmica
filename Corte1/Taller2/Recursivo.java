import java.util.Scanner;

public class Recursivo {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.println("Hola ingrese el numero que funcionara como potencia de 2");

		int n = sc.nextInt();
		long inicio = System.nanoTime();

		for (int i = 0; i <= n; i++) {

			System.out.println("2^" + i + " = " + (calcularPotenciaRecursividad(2, i)));
		}

		long finalizacion = System.nanoTime();

		long duracion = (finalizacion - inicio);

		System.out.println();

		System.out.println("El algoritmo se ejecuto en: " + duracion + " nanosegundos");

		sc.close();
	}
	public static long calcularPotenciaRecursividad(int base, int exponente) {
		if (exponente == 0) {
			return 1;
		} else {
			return base * calcularPotenciaRecursividad(base, exponente - 1);
		}
	}
	
}
