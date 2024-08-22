import java.util.*;

public class Main
{  
  public static void main( String[] args ){
    Scanner entrada = new Scanner(System.in);
    System.out.print("Valor de -n-: ");
    int n = entrada.nextInt();
    for(int exp=0; exp<= n; exp++){
      System.out.println(" 2 Elevado a "+ exp + " igual a "+ (1 << exp));
    }
   }
}  
  
