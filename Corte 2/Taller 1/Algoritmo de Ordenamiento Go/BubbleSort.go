package main

import (
    "fmt"
    "math/rand"
    "time"
)

const N = 1000

func bubbleSort(arr []int, comparisons *int, swaps *int) {
    for i := 0; i < N-1; i++ {
        for j := 0; j < N-i-1; j++ {
            (*comparisons)++
            if arr[j] < arr[j+1] { // Cambio aquí: arr[j] < arr[j+1]
                // Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                (*swaps)++
            }
        }
    }
}

func main() {
    rand.Seed(time.Now().UnixNano())

    // Generar números aleatorios de 0 a 9
    arr := make([]int, N)
    for i := range arr {
        arr[i] = rand.Intn(10) // Números entre 0 y 9
    }

    // Mostrar números generados
    fmt.Println("Numeros generados:")
    for _, num := range arr {
        fmt.Printf("%d ", num)
    }
    fmt.Println()

    var comparisons int = 0
    var swaps int = 0

    // Ordenar usando el algoritmo de burbuja
    bubbleSort(arr, &comparisons, &swaps)

    // Mostrar números ordenados
    fmt.Println("Numeros ordenados:")
    for _, num := range arr {
        fmt.Printf("%d ", num)
    }
    fmt.Println()

    // Mostrar resultados
    fmt.Printf("Comparaciones: %d\n", comparisons)
    fmt.Printf("Intercambios: %d\n", swaps)
    fmt.Println("Estable: Si")
    fmt.Println("Insercion: No")
}