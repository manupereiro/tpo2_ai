# astar.py
# Búsqueda A* (A-Star Search)
# Implementación para el Trabajo Práctico 2 - IA

from util import PriorityQueue

def a_star_search(problem, heuristic):
    """
    Búsqueda A* (A-Star)
    
    Combina el costo real del camino (g) con una estimación heurística del costo
    restante (h) para guiar la búsqueda de manera eficiente hacia el objetivo.
    
    Función de evaluación: f(n) = g(n) + h(n)
    - g(n): costo real desde el inicio hasta el nodo n
    - h(n): estimación heurística del costo desde n hasta el objetivo
    
    Características:
    - Garantiza encontrar la solución óptima si la heurística es admisible
    - Más eficiente que UCS cuando se usa una buena heurística
    - La calidad de la heurística determina la eficiencia del algoritmo
    - Complejidad depende de la calidad de la heurística
    
    Args:
        problem: Objeto que implementa la interfaz SearchProblem
        heuristic: Función heurística que estima el costo al objetivo
    
    Returns:
        list: Lista de acciones que lleva del estado inicial al objetivo
    """
    
    # Usar una cola de prioridad (PriorityQueue) para A*
    # La prioridad está determinada por f(n) = g(n) + h(n)
    priority_queue = PriorityQueue()
    
    # Inicializar la cola de prioridad con el estado inicial
    # Cada elemento es una tupla (estado, lista_de_acciones, costo_acumulado)
    # La prioridad es f(n) = g(n) + h(n)
    start_state = problem.getStartState()
    start_heuristic = heuristic(start_state, problem)
    priority_queue.push((start_state, [], 0), start_heuristic)
    
    # Conjunto para llevar registro de estados visitados (evita ciclos)
    visited = set()
    
    # Bucle principal del algoritmo
    while not priority_queue.isEmpty():
        # Obtener el estado con menor f(n) = g(n) + h(n)
        current_state, actions, total_cost = priority_queue.pop()
        
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
                new_cost = total_cost + step_cost  # g(n)
                # Calcular f(n) = g(n) + h(n)
                h_cost = heuristic(successor, problem)  # h(n)
                f_cost = new_cost + h_cost  # f(n)
                # Agregar a la cola con prioridad = f(n)
                priority_queue.push((successor, new_actions, new_cost), f_cost)
    
    # Si no se encuentra solución, retornar lista vacía
    return []

def null_heuristic(state, problem=None):
    """
    Heurística nula - siempre retorna 0
    Con esta heurística, A* se comporta igual que UCS
    """
    return 0

def manhattan_heuristic(position, problem, info={}):
    """
    Heurística de distancia de Manhattan
    Calcula la distancia de Manhattan entre la posición actual y el objetivo
    """
    x1, y1 = position
    x2, y2 = problem.goal
    return abs(x1 - x2) + abs(y1 - y2)

def ejemplo_uso():
    """
    Ejemplo de cómo usar el algoritmo A* en Pacman
    """
    print("=== Búsqueda A* (A-Star) ===")
    print("Comando para ejecutar en Pacman:")
    print("python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic")
    print("\nCaracterísticas del A*:")
    print("- Combina costo real + estimación heurística")
    print("- Garantiza solución óptima (heurística admisible)")
    print("- Más eficiente que UCS con buena heurística")
    print("- f(n) = g(n) + h(n)")
    print("\nHeurísticas comunes:")
    print("- Manhattan: |x1-x2| + |y1-y2|")
    print("- Euclidiana: sqrt((x1-x2)² + (y1-y2)²)")

if __name__ == "__main__":
    ejemplo_uso() 