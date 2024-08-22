import java.util.Scanner;

public class Trabajo {

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

	}

	public static long calcularPotenciaRecursividad(int base, int exponente) {

		long resultado = 1;

		for (int i = 0; i < exponente; i++) {

			resultado *= base;

		}

		return resultado;

	}

}
