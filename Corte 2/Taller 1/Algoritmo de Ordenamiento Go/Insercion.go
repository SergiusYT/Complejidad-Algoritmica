package main

import (
    "fmt"
    "math/rand"
    "time"
)

const N = 1000

func insertionSort(arr []int, comparisons *int, swaps *int) {
    for i := 1; i < N; i++ {
        key := arr[i]
        j := i - 1

        // Comparar e insertar
        for j >= 0 && arr[j] < key {
            (*comparisons)++
            arr[j+1] = arr[j]
            j--
            (*swaps)++
        }
        arr[j+1] = key
        (*swaps)++
    }
}

func main() {
    // Inicializar la semilla para números aleatorios
    rand.Seed(time.Now().UnixNano())

    // Generar números aleatorios entre 0 y 9
    arr := make([]int, N)
    for i := range arr {
        arr[i] = rand.Intn(10) // Números entre 0 y 9
    }

    // Mostrar números generados
    fmt.Println("Números generados:")
    for _, num := range arr {
        fmt.Printf("%d ", num)
    }
    fmt.Println()

    var comparisons int = 0
    var swaps int = 0

    // Ordenar usando el algoritmo de inserción
    insertionSort(arr, &comparisons, &swaps)

    // Mostrar números ordenados
    fmt.Println("Números ordenados:")
    for _, num := range arr {
        fmt.Printf("%d ", num)
    }
    fmt.Println()

   
    fmt.Printf("Comparaciones: %d\n", comparisons)
    fmt.Printf("Intercambios: %d\n", swaps)
    fmt.Println("Estable: Sí")
    fmt.Println("Inserción: Sí")
}