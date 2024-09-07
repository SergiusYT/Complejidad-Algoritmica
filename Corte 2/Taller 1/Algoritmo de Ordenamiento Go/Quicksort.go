package main

import (
	"fmt"
	"math/rand"
	"time"
)

const N = 9000

func partition(arr []int, low int, high int, comparisons *int, swaps *int) int {
	pivot := arr[high]
	i := low - 1

	for j := low; j <= high-1; j++ {
		(*comparisons)++
		if arr[j] > pivot { // Cambio aquí: arr[j] > pivot
			i++
			// Swap
			arr[i], arr[j] = arr[j], arr[i]
			(*swaps)++
		}
	}

	arr[i+1], arr[high] = arr[high], arr[i+1]
	(*swaps)++
	return i + 1
}

func quickSort(arr []int, low int, high int, comparisons *int, swaps *int) {
	if low < high {
		pi := partition(arr, low, high, comparisons, swaps)
		quickSort(arr, low, pi-1, comparisons, swaps)
		quickSort(arr, pi+1, high, comparisons, swaps)
	}
}

func main() {

	rand.Seed(time.Now().UnixNano())
	// Medir el tiempo de ejecución en nanosegundos
	start := time.Now()

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

	// Ordenar usando el algoritmo QuickSort
	quickSort(arr, 0, N-1, &comparisons, &swaps)

	// Calcular la duración
	duration := time.Since(start)

	// Mostrar números ordenados
	fmt.Println("Numeros ordenados:")
	for _, num := range arr {
		fmt.Printf("%d ", num)
	}
	fmt.Println()

	// Mostrar resultados
	fmt.Printf("Comparaciones: %d\n", comparisons)
	fmt.Printf("Intercambios: %d\n", swaps)
	fmt.Println("Estable: No")
	fmt.Println("Insercion: No")
	// Mostrar el tiempo de ejecución en nanosegundos
	fmt.Printf("Tiempo de ejecución en nanosegundos: %d\n", duration.Nanoseconds())
}
