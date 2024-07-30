using System;
using System.Windows.Forms;

public class Taller
{
    [STAThread]
    public static void Main(string[] args)
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Ejecutar();
    }

    public static void Ejecutar()
    {
        int baseNumero = PedirNumero("Primer número (base): ");
        while (baseNumero == 0)
        {
            MessageBox.Show("El primer número no puede ser cero.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            baseNumero = PedirNumero("Ingrese de nuevo el primer número (base): ");
        }

        int exponente = PedirNumero("Segundo número (exponente): ");
        
        string resultados = CalcularPotencias(baseNumero, exponente);
        MessageBox.Show(resultados, "Resultados", MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    public static int PedirNumero(string mensaje)
    {
        string input = Microsoft.VisualBasic.Interaction.InputBox(mensaje, "Entrada de datos", "0");
        return int.Parse(input);
    }

    public static string CalcularPotencias(int baseNumero, int exponente)
    {
        System.Text.StringBuilder resultados = new System.Text.StringBuilder();
        for (int i = 0; i <= exponente; i++)
        {
            int resultado = Potenciar(baseNumero, i);
            resultados.Append(baseNumero + "^" + i + " = " + resultado + "\n");
        }
        return resultados.ToString();
    }

    public static int Potenciar(int baseNumero, int exponente)
    {
        int resultado = 1;
        for (int i = 1; i <= exponente; i++)
        {
            resultado *= baseNumero;
        }
        return resultado;
    }
}
