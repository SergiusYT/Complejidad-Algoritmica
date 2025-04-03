require 'rgl/adjacency'
require 'rgl/dot'

# Datos del problema de distancias entre nodos
DISTANCIAS = {
  'A' => { 'B' => 10, 'C' => 12, 'D' => 15, 'E' => 11, 'F' => 20 },
  'B' => { 'A' => 10, 'C' => 9,  'D' => 7,  'E' => 13, 'F' => 14 },
  'C' => { 'A' => 12, 'B' => 9,  'D' => 8,  'E' => 6,  'F' => 15 },
  'D' => { 'A' => 15, 'B' => 7,  'C' => 8,  'E' => 5,  'F' => 9  },
  'E' => { 'A' => 11, 'B' => 13, 'C' => 6,  'D' => 5,  'F' => 7  },
  'F' => { 'A' => 20, 'B' => 14, 'C' => 15, 'D' => 9,  'E' => 7  }
}

# Variables para almacenar la mejor ruta y su distancia
@mejor_distancia = Float::INFINITY
@mejor_ruta = []

# Contador para hacer único cada nodo visitado
@contador_nodos = 0

# Crear el arbol dirigido
arbol = RGL::DirectedAdjacencyGraph.new

# Método recursivo para construir el árbol y registrar la poda
def ramificacion_y_poda(nodo_actual, visitados, distancia_actual, camino, arbol, nodo_padre = nil)
  # Generar un identificador único para el nodo que incluya la distancia acumulada
  @contador_nodos += 1
  nodo_unico = "#{nodo_actual}_#{distancia_actual}km_#{@contador_nodos}"

  # Añadir nodo al arbol con el identificador único
  arbol.add_vertex(nodo_unico)

  # Añadir arista al arbol con la distancia entre nodos como etiqueta, si hay un nodo padre
  if nodo_padre
    arbol.add_edge(nodo_padre, nodo_unico)
  end

  # Si se han visitado todas las ciudades, cerrar el ciclo volviendo a 'A'
  if visitados.size == DISTANCIAS.size
    distancia_total = distancia_actual + DISTANCIAS[nodo_actual]['A']
    
    # Crear nodo de retorno a A con su distancia
    @contador_nodos += 1
    nodo_a_retorno = "A_#{distancia_total}km_#{@contador_nodos}"
    arbol.add_vertex(nodo_a_retorno)
    arbol.add_edge(nodo_unico, nodo_a_retorno)

    # Imprimir la cota estimada para esta ruta
    puts "Cota estimada para la ruta #{(camino + ['A']).join(' -> ')}: #{distancia_total} km"

    if distancia_total < @mejor_distancia
      @mejor_distancia = distancia_total
      @mejor_ruta = camino + ['A']
    end
    return
  end

  # Explorar los localidades del nodo actual
  DISTANCIAS[nodo_actual].each do |siguiente_nodo, distancia|
    unless visitados.include?(siguiente_nodo)
      nueva_distancia = distancia_actual + distancia

      if nueva_distancia < @mejor_distancia
        # Continuar explorando si encontramos una mejor ruta
        ramificacion_y_poda(siguiente_nodo, visitados + [siguiente_nodo], nueva_distancia, camino + [siguiente_nodo], arbol, nodo_unico)
      else
        # Registrar una rama podada con el prefijo "(PODADO)" en el nodo
        nodo_podado = "#{siguiente_nodo}_#{distancia_actual}km_#{@contador_nodos + 1} (PODADO)"
        arbol.add_vertex(nodo_podado)
        arbol.add_edge(nodo_unico, nodo_podado)  # Añadir arista entre nodo actual y el nodo podado
        puts "Poda de la ruta #{(camino + [siguiente_nodo]).join(' -> ')} con distancia estimada: #{nueva_distancia} km"
      end
    end
  end
end

# Iniciar la búsqueda desde el nodo 'A'
ramificacion_y_poda('A', ['A'], 0, ['A'], arbol)

# Exportar el arbol a un archivo DOT
arbol.write_to_graphic_file('png', 'arbol_rutas_con_kilometraje')

# Imprimir la mejor ruta encontrada
puts "Mejor ruta encontrada: #{@mejor_ruta.join(' -> ')} con distancia #{@mejor_distancia} km."
