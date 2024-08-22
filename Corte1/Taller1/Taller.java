import javax.swing.JOptionPane;

public class Taller {
    public static void main(String[] args) {
        ejecutar();
    }

    public static void ejecutar() {
        long startTime = System.nanoTime();  // Tiempo inicial

        long base = Long.parseLong(JOptionPane.showInputDialog("Primer número (base): "));
        while (base == 0) {
            base = Long.parseLong(JOptionPane.showInputDialog(null, "El primer número no puede ser cero. Ingrese de nuevo: ", "Error", JOptionPane.ERROR_MESSAGE));
        }

        int exponente = Integer.parseInt(JOptionPane.showInputDialog("Segundo número (exponente): "));

        StringBuilder resultados = new StringBuilder();
        for (int i = 0; i <= exponente; i++) {
            long resultado = potenciar(base, i);
            resultados.append(base).append("^").append(i).append(" = ").append(resultado).append("\n");
        }

        long endTime = System.nanoTime();  // Tiempo final
        long duration = endTime - startTime;  // Duración en nanosegundos

        // Mostrar resultados y tiempo de ejecución
        JOptionPane.showMessageDialog(null, resultados.toString() + "\nTiempo de ejecución: " + duration + " nanosegundos");
    }

    public static long potenciar(long base, int exponente) {
        long resultado = 1;
        for (int i = 1; i <= exponente; i++) {
            resultado *= base;
        }
        return resultado;
    }
}
