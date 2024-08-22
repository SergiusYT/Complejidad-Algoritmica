import java.util.Scanner;
import java.lang.Math;
public class Taller2 {
	

	  public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);

	    System.out.print("Ingrese un número entero positivo <= 20: ");
	    int n = scanner.nextInt();

	    if (n <= 0 || n > 20) {
	      System.out.println("Error: El número debe ser entero positivo y menor o igual a 20.");
	      return;
	    }

	    for (int i = 0; i <= n; i++) {
	       int resultado = (int) Math.pow(2, i);
	      System.out.println("2 ^ " + i + " = " + resultado);
	    }
	  }
	

}
