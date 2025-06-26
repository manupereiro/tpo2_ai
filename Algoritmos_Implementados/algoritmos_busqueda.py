# algoritmos_busqueda.py
# Demostración de los algoritmos de búsqueda implementados
# Trabajo Práctico 2 - Inteligencia Artificial

import os
import sys

def mostrar_menu():
    """
    Muestra el menú principal con las opciones de algoritmos
    """
    print("=" * 60)
    print("   ALGORITMOS DE BÚSQUEDA - PACMAN")
    print("   Trabajo Práctico 2 - Inteligencia Artificial")
    print("=" * 60)
    print()
    print("Algoritmos implementados:")
    print("1. DFS - Búsqueda en Profundidad (Depth-First Search)")
    print("2. BFS - Búsqueda en Anchura (Breadth-First Search)")
    print("3. UCS - Búsqueda de Costo Uniforme (Uniform Cost Search)")
    print("4. A*  - Búsqueda A* (A-Star Search)")
    print("5. Ejecutar todas las pruebas")
    print("6. Salir")
    print()

def ejecutar_algoritmo(opcion):
    """
    Ejecuta el algoritmo seleccionado en diferentes laberintos
    """
    # Cambiar al directorio padre para ejecutar pacman
    os.chdir("..")
    
    comandos = {
        "1": [
            ("DFS en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs"),
            ("DFS en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs")
        ],
        "2": [
            ("BFS en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs"),
            ("BFS en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs"),
            ("BFS en BigMaze", "python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=bfs")
        ],
        "3": [
            ("UCS en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs"),
            ("UCS en BigMaze", "python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=ucs")
        ],
        "4": [
            ("A* en BigMaze con Manhattan", "python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a \"fn=astar,heuristic=manhattanHeuristic\""),
            ("A* en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a \"fn=astar,heuristic=manhattanHeuristic\"")
        ]
    }
    
    if opcion in comandos:
        for descripcion, comando in comandos[opcion]:
            print(f"\n--- {descripcion} ---")
            print(f"Comando: {comando}")
            print("📂 Ejecutándose desde: Codigo Fuente/")
            input("Presiona Enter para ejecutar...")
            os.system(comando)
            input("Presiona Enter para continuar...")
    
    # Volver al directorio de algoritmos
    os.chdir("Algoritmos_Implementados")

def mostrar_teoria_algoritmos():
    """
    Muestra la teoría detrás de cada algoritmo
    """
    print("\n" + "=" * 60)
    print("   TEORÍA DE LOS ALGORITMOS DE BÚSQUEDA")
    print("=" * 60)
    
    print("\n1. DFS (Depth-First Search) - Búsqueda en Profundidad:")
    print("   • Explora tan profundo como sea posible antes de retroceder")
    print("   • Usa una PILA (LIFO - Last In, First Out)")
    print("   • No garantiza la solución óptima")
    print("   • Complejidad temporal: O(b^m)")
    print("   • Complejidad espacial: O(bm)")
    print("   • Mejor para: Problemas con soluciones profundas")
    
    print("\n2. BFS (Breadth-First Search) - Búsqueda en Anchura:")
    print("   • Explora nivel por nivel")
    print("   • Usa una COLA (FIFO - First In, First Out)")
    print("   • Garantiza la solución óptima (costos uniformes)")
    print("   • Complejidad temporal: O(b^d)")
    print("   • Complejidad espacial: O(b^d)")
    print("   • Mejor para: Encontrar caminos más cortos")
    
    print("\n3. UCS (Uniform Cost Search) - Búsqueda de Costo Uniforme:")
    print("   • Explora el nodo con menor costo acumulado")
    print("   • Usa una COLA DE PRIORIDAD ordenada por costo")
    print("   • Garantiza la solución óptima")
    print("   • Generalización de BFS para costos variables")
    print("   • Mejor para: Problemas con costos de acciones diferentes")
    
    print("\n4. A* (A-Star Search) - Búsqueda A*:")
    print("   • Combina costo real + estimación heurística")
    print("   • Usa una COLA DE PRIORIDAD ordenada por f(n) = g(n) + h(n)")
    print("   • g(n): costo real, h(n): heurística")
    print("   • Garantiza solución óptima (heurística admisible)")
    print("   • Más eficiente que UCS con buena heurística")
    print("   • Mejor para: Búsquedas dirigidas hacia un objetivo conocido")

def ejecutar_todas_pruebas():
    """
    Ejecuta una secuencia de pruebas para comparar todos los algoritmos
    """
    print("\n--- EJECUTANDO TODAS LAS PRUEBAS ---")
    
    # Cambiar al directorio padre
    os.chdir("..")
    
    pruebas = [
        ("DFS en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs"),
        ("BFS en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs"),
        ("UCS en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs"),
        ("A* en TinyMaze", "python pacman.py -l tinyMaze -p SearchAgent -a \"fn=astar,heuristic=manhattanHeuristic\""),
        ("BFS en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs"),
        ("UCS en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs"),
        ("A* en MediumMaze", "python pacman.py -l mediumMaze -p SearchAgent -a \"fn=astar,heuristic=manhattanHeuristic\"")
    ]
    
    for descripcion, comando in pruebas:
        print(f"\n--- {descripcion} ---")
        print(f"Comando: {comando}")
        input("Presiona Enter para ejecutar...")
        os.system(comando)
    
    # Volver al directorio de algoritmos
    os.chdir("Algoritmos_Implementados")

def main():
    """
    Función principal del programa
    """
    print("📂 Ejecutándose desde: Algoritmos_Implementados/")
    print("🎮 Juego Pacman en: ../")
    print("📍 Implementación principal: ../search.py")
    print()
    
    while True:
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "6":
            print("¡Gracias por usar el sistema de algoritmos de búsqueda!")
            break
        elif opcion == "5":
            ejecutar_todas_pruebas()
        elif opcion in ["1", "2", "3", "4"]:
            ejecutar_algoritmo(opcion)
        elif opcion.lower() == "teoria":
            mostrar_teoria_algoritmos()
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        input("\nPresiona Enter para volver al menú principal...")

if __name__ == "__main__":
    print("🧠 Iniciando sistema de demostración de algoritmos de búsqueda...")
    print("💡 Tip: Puedes escribir 'teoria' en cualquier momento para ver la explicación teórica")
    print()
    main() 