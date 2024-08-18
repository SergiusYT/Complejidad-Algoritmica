import java.math.BigInteger;
import java.util.Scanner;

public class Potencia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa un numero entero positivo para la base: ");
        BigInteger base = scanner.nextBigInteger();

        System.out.print("Ingresa el exponente maximo entero positivo: ");
        int exponenteMaximo = scanner.nextInt();

        BigInteger resultado = BigInteger.ONE; 
        for (int i = 0; i <= exponenteMaximo; i++) {
            System.out.println(base + "^" + i + " = " + resultado);
            resultado = resultado.multiply(base);
        }

        scanner.close();
    }
}
