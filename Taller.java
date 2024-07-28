import javax.swing.JOptionPane;

public class Taller{
    public static void main(String[] args) {
        ejecutar();
    }


    public static void ejecutar() {
        
        int base = Integer.parseInt(JOptionPane.showInputDialog("Primer número (base): "));
        while (base == 0) {
            base = Integer.parseInt(JOptionPane.showInputDialog(null, "El primer número no puede ser cero. Ingrese de nuevo: ", "Error", JOptionPane.ERROR_MESSAGE));
        }

   
        int exponente = Integer.parseInt(JOptionPane.showInputDialog("Segundo número (exponente): "));

       
        StringBuilder resultados = new StringBuilder();
        for (int i = 0; i <= exponente; i++) {
            int resultado = potencia(base, i);
            resultados.append(base).append("^").append(i).append(" = ").append(resultado).append("\n");
        }

        JOptionPane.showMessageDialog(null, resultados.toString());
    }


    public static int potencia(int base, int exponente) {
        int resultado = 1;
        for (int i = 1; i <= exponente; i++) {
            resultado *= base;
        }
        return resultado;
    }
}