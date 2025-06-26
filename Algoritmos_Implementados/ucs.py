# ucs.py
# Búsqueda de Costo Uniforme (Uniform Cost Search)
# Implementación para el Trabajo Práctico 2 - IA

from util import PriorityQueue

def uniform_cost_search(problem):
    """
    Búsqueda de Costo Uniforme (UCS)
    
    Explora el nodo con menor costo acumulado primero. Utiliza una cola de prioridad
    donde la prioridad está determinada por el costo total del camino.
    
    Características:
    - Garantiza encontrar la solución óptima cuando los costos son no negativos
    - Es una generalización de BFS que considera costos variables
    - Explora nodos en orden de costo creciente
    - Complejidad temporal: O(b^(C*/ε)) donde C* es el costo óptimo y ε el costo mínimo
    - Complejidad espacial: O(b^(C*/ε))
    
    Args:
        problem: Objeto que implementa la interfaz SearchProblem
    
    Returns:
        list: Lista de acciones que lleva del estado inicial al objetivo con costo mínimo
    """
    
    # Usar una cola de prioridad (PriorityQueue) para UCS
    # La prioridad está determinada por el costo acumulado
    priority_queue = PriorityQueue()
    
    # Inicializar la cola de prioridad con el estado inicial
    # Cada elemento es una tupla (estado, lista_de_acciones, costo_acumulado)
    # La prioridad es el costo acumulado
    start_state = problem.getStartState()
    priority_queue.push((start_state, [], 0), 0)
    
    # Conjunto para llevar registro de estados visitados (evita ciclos)
    visited = set()
    
    # Bucle principal del algoritmo
    while not priority_queue.isEmpty():
        # Obtener el estado con menor costo acumulado
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
                new_cost = total_cost + step_cost
                # Agregar a la cola con prioridad = costo total
                priority_queue.push((successor, new_actions, new_cost), new_cost)
    
    # Si no se encuentra solución, retornar lista vacía
    return []

def ejemplo_uso():
    """
    Ejemplo de cómo usar el algoritmo UCS en Pacman
    """
    print("=== Búsqueda de Costo Uniforme (UCS) ===")
    print("Comando para ejecutar en Pacman:")
    print("python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs")
    print("\nCaracterísticas del UCS:")
    print("- Explora por costo acumulado mínimo")
    print("- Garantiza solución óptima")
    print("- Considera costos variables de las acciones")
    print("- Es una generalización de BFS")

if __name__ == "__main__":
    ejemplo_uso() 