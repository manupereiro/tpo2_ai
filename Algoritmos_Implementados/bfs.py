# bfs.py
# Búsqueda en Anchura (Breadth-First Search)
# Implementación para el Trabajo Práctico 2 - IA

from util import Queue

def breadth_first_search(problem):
    """
    Búsqueda en Anchura (BFS)
    
    Explora el árbol de búsqueda nivel por nivel, visitando todos los nodos
    de un nivel antes de pasar al siguiente. Utiliza una cola (FIFO).
    
    Características:
    - Garantiza encontrar la solución óptima en problemas con costos uniformes
    - Explora sistemáticamente por niveles
    - Requiere más memoria que DFS
    - Complejidad temporal: O(b^d) donde b es el factor de ramificación y d la profundidad de la solución
    - Complejidad espacial: O(b^d)
    
    Args:
        problem: Objeto que implementa la interfaz SearchProblem
    
    Returns:
        list: Lista de acciones que lleva del estado inicial al objetivo
    """
    
    # Usar una cola (Queue) para BFS - First In, First Out
    queue = Queue()
    
    # Inicializar la cola con el estado inicial
    # Cada elemento de la cola es una tupla (estado, lista_de_acciones)
    start_state = problem.getStartState()
    queue.push((start_state, []))
    
    # Conjunto para llevar registro de estados visitados (evita ciclos)
    visited = set()
    
    # Bucle principal del algoritmo
    while not queue.isEmpty():
        # Obtener el próximo estado a explorar (el más antiguo agregado)
        current_state, actions = queue.pop()
        
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
                queue.push((successor, new_actions))
    
    # Si no se encuentra solución, retornar lista vacía
    return []

def ejemplo_uso():
    """
    Ejemplo de cómo usar el algoritmo BFS en Pacman
    """
    print("=== Búsqueda en Anchura (BFS) ===")
    print("Comando para ejecutar en Pacman:")
    print("python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs")
    print("\nCaracterísticas del BFS:")
    print("- Explora nivel por nivel")
    print("- Garantiza solución óptima (costos uniformes)")
    print("- Usa más memoria que DFS")
    print("- Ideal para encontrar caminos más cortos")

if __name__ == "__main__":
    ejemplo_uso() 