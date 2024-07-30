const prompt = require('prompt-sync')();

function potenciar(base, exponente) {
    let resultado = 1;
    for (let i = 1; i <= exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

function ejecutar() {
    let base = parseInt(prompt("Primer número (base): "), 10);
    while (base === 0) {
        base = parseInt(prompt("El primer número no puede ser cero. Ingrese de nuevo: "), 10);
    }

    let exponente = parseInt(prompt("Segundo número (exponente): "), 10);

    let resultados = '';
    for (let i = 0; i <= exponente; i++) {
        let resultado = potenciar(base, i);
        resultados += `${base}^${i} = ${resultado}\n`;
    }

    console.log(resultados);
}

ejecutar();
