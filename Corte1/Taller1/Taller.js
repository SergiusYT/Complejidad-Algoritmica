const { app, BrowserWindow, dialog } = require('electron');
const { performance } = require('perf_hooks');
const prompt = require('electron-prompt'); // Importar electron-prompt

// Función para potenciar
function potenciar(base, exponente) {
    let resultado = 1;
    for (let i = 1; i <= exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

// Función para solicitar entradas y mostrar resultados
async function ejecutar() {
    try {
        let tiempoInicio = performance.now();

        // Solicitar base
        let base = parseInt(await prompt({
            title: 'Entrada de Datos',
            label: 'Primer número (base):',
            type: 'input',
            inputAttrs: {
                type: 'text'
            }
        }), 10);

        while (base === 0 || isNaN(base)) {
            await dialog.showErrorBox('Error', 'El primer número no puede ser cero. Ingrese de nuevo.');
            base = parseInt(await prompt({
                title: 'Entrada de Datos',
                label: 'Ingrese de nuevo el primer número (base):',
                type: 'input',
                inputAttrs: {
                    type: 'text'
                }
            }), 10);
        }

        // Solicitar exponente
        let exponente = parseInt(await prompt({
            title: 'Entrada de Datos',
            label: 'Segundo número (exponente):',
            type: 'input',
            inputAttrs: {
                type: 'text'
            }
        }), 10);

        // Procesar datos
        let resultados = '';

        for (let i = 0; i <= exponente; i++) {
            let resultado = potenciar(base, i);
            resultados += `${base}^${i} = ${resultado}\n`;
        }

        let tiempoFin = performance.now();
        let tiempoEjecucion = (tiempoFin - tiempoInicio) * 1e6; // Convertir a nanosegundos

        // Mostrar resultados
        await dialog.showMessageBox({
            type: 'info',
            title: 'Resultados',
            message: `${resultados}\nTiempo de ejecución: ${tiempoEjecucion.toFixed(0)} nanosegundos`
        });
    } catch (err) {
        console.error('Error durante la ejecución:', err);
    } finally {
        app.quit(); // Cerrar la aplicación después de mostrar los resultados
    }
}

app.whenReady().then(() => {
    // Crear una ventana oculta
    const ventana = new BrowserWindow({
        show: false, // Ocultar la ventana
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    ventana.loadURL('data:text/html,<html><body></body></html>'); // Cargar una página en blanco para evitar errores

    // Ejecutar la función principal
    ejecutar();
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
