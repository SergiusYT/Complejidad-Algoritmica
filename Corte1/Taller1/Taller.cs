using System;
using System.Diagnostics;
using System.Text;
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
        var startTime = DateTime.Now; // Tiempo inicial
        long baseNumero = 0;
        while (baseNumero == 0)
        {
            string baseInput = Microsoft.VisualBasic.Interaction.InputBox("Primer número (base): ", "Entrada de datos", "0");
            if (long.TryParse(baseInput, out baseNumero))
            {
                if (baseNumero == 0)
                {
                    MessageBox.Show("El primer número no puede ser cero. Ingrese de nuevo.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    baseNumero = 0; // Restablecer el valor si la entrada es inválida
                }
            }
            else
            {
                var result = MessageBox.Show("¿Seguro que quiere salir del programa?", "Salir", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (result == DialogResult.Yes)
                {
                    return;
                }
            }
        }

        string exponenteInput = Microsoft.VisualBasic.Interaction.InputBox("Segundo número (exponente): ", "Entrada de datos", "0");
        if (!int.TryParse(exponenteInput, out int exponente))
        {
            var result = MessageBox.Show("¿Seguro que quiere salir del programa?", "Salir", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                return;
            }
        }

        StringBuilder resultados = new StringBuilder();
        for (int i = 0; i <= exponente; i++)
        {
            long resultado = Potenciar(baseNumero, i);
            resultados.Append($"{baseNumero}^{i} = {resultado}\n");
        }

        var endTime = DateTime.Now; // Tiempo final
        var duration = (endTime - startTime).TotalMilliseconds * 1e6; // Duración en nanosegundos

        resultados.Append($"\nTiempo de ejecución: {duration} nanosegundos");
        MessageBox.Show(resultados.ToString(), "Resultados", MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    public static long Potenciar(long baseNumero, int exponente)
    {
        long resultado = 1;
        for (int i = 1; i <= exponente; i++)
        {
            resultado *= baseNumero;
        }
        return resultado;
    }
}
