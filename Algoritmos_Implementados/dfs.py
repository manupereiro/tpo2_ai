# dfs.py
# Búsqueda en Profundidad (Depth-First Search)
# Implementación para el Trabajo Práctico 2 - IA

import sys
import os
# Agregar la carpeta padre al path para poder importar util
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from util import Stack
except ImportError:
    print("⚠️  Para ejecutar este archivo individualmente, necesitas estar en la carpeta 'Codigo Fuente'")
    print("💡 Usa: cd .. && python Algoritmos_Implementados/dfs.py")
    print("🎮 O mejor aún, ejecuta los algoritmos en Pacman:")
    print("   python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs")
    sys.exit(1)

def depth_first_search(problem):
    """
    Búsqueda en Profundidad (DFS)
    
    Explora el árbol de búsqueda en profundidad, yendo tan profundo como sea posible
    antes de retroceder. Utiliza una pila (LIFO) para mantener los nodos por explorar.
    
    Características:
    - No garantiza encontrar la solución óptima
    - Puede quedar atrapado en bucles infinitos si no se controlan los estados visitados
    - Requiere menos memoria que BFS en árboles muy anchos
    - Complejidad temporal: O(b^m) donde b es el factor de ramificación y m la profundidad máxima
    - Complejidad espacial: O(bm)
    
    Args:
        problem: Objeto que implementa la interfaz SearchProblem
    
    Returns:
        list: Lista de acciones que lleva del estado inicial al objetivo
    """
    
    # Usar una pila (Stack) para DFS - Last In, First Out
    stack = Stack()
    
    # Inicializar la pila con el estado inicial
    # Cada elemento de la pila es una tupla (estado, lista_de_acciones)
    start_state = problem.getStartState()
    stack.push((start_state, []))
    
    # Conjunto para llevar registro de estados visitados (evita ciclos)
    visited = set()
    
    # Bucle principal del algoritmo
    while not stack.isEmpty():
        # Obtener el próximo estado a explorar (el más reciente agregado)
        current_state, actions = stack.pop()
        
        # Si ya visitamos este estado, continuamos con el siguiente
        if current_state in visited:
            continue
            
        # Marcar el estado actual como visitado
        visited.add(current_state)
        
        # Verificar si hemos llegado al objetivo
        if problem.isGoalState(current_state):
            return actions
            
        # Expandir el estado actual obteniendo todos sus sucesores
        for successor, action, step_cost in problem.getSuccessors(current_state):
            # Solo agregar sucesores no visitados
            if successor not in visited:
                new_actions = actions + [action]
                stack.push((successor, new_actions))
    
    # Si no se encuentra solución, retornar lista vacía
    return []

def ejemplo_uso():
    """
    Ejemplo de cómo usar el algoritmo DFS en Pacman
    """
    print("=== Búsqueda en Profundidad (DFS) ===")
    print("Comando para ejecutar en Pacman:")
    print("python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs")
    print("\nCaracterísticas del DFS:")
    print("- Explora en profundidad primero")
    print("- No garantiza solución óptima")
    print("- Usa menos memoria que BFS")
    print("- Puede ser más rápido en algunos casos")
    print("\n" + "="*50)
    print("📍 UBICACIÓN: Algoritmos_Implementados/dfs.py")
    print("🎮 FUNCIONAL: ../search.py (líneas 75-110)")
    print("="*50)

if __name__ == "__main__":
    ejemplo_uso() 