# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
    # Usar una pila (Stack) para DFS
    from util import Stack
    
    # Inicializar la pila con el estado inicial
    # Cada elemento de la pila es una tupla (estado, lista_de_acciones)
    stack = Stack()
    start_state = problem.getStartState()
    stack.push((start_state, []))
    
    # Conjunto para llevar registro de estados visitados
    visited = set()
    
    while not stack.isEmpty():
        current_state, actions = stack.pop()
        
        # Si ya visitamos este estado, continuamos
        if current_state in visited:
            continue
            
        # Marcar el estado actual como visitado
        visited.add(current_state)
        
        # Verificar si hemos llegado al objetivo
        if problem.isGoalState(current_state):
            return actions
            
        # Expandir el estado actual
        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_actions = actions + [action]
                stack.push((successor, new_actions))
    
    # Si no se encuentra solución
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    # Usar una cola (Queue) para BFS
    from util import Queue
    
    # Inicializar la cola con el estado inicial
    # Cada elemento de la cola es una tupla (estado, lista_de_acciones)
    queue = Queue()
    start_state = problem.getStartState()
    queue.push((start_state, []))
    
    # Conjunto para llevar registro de estados visitados
    visited = set()
    
    while not queue.isEmpty():
        current_state, actions = queue.pop()
        
        # Si ya visitamos este estado, continuamos
        if current_state in visited:
            continue
            
        # Marcar el estado actual como visitado
        visited.add(current_state)
        
        # Verificar si hemos llegado al objetivo
        if problem.isGoalState(current_state):
            return actions
            
        # Expandir el estado actual
        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_actions = actions + [action]
                queue.push((successor, new_actions))
    
    # Si no se encuentra solución
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    # Usar una cola de prioridad (PriorityQueue) para UCS
    from util import PriorityQueue
    
    # Inicializar la cola de prioridad con el estado inicial
    # Cada elemento es una tupla (estado, lista_de_acciones, costo_acumulado)
    # La prioridad es el costo acumulado
    priority_queue = PriorityQueue()
    start_state = problem.getStartState()
    priority_queue.push((start_state, [], 0), 0)
    
    # Conjunto para llevar registro de estados visitados
    visited = set()
    
    while not priority_queue.isEmpty():
        current_state, actions, total_cost = priority_queue.pop()
        
        # Si ya visitamos este estado, continuamos
        if current_state in visited:
            continue
            
        # Marcar el estado actual como visitado
        visited.add(current_state)
        
        # Verificar si hemos llegado al objetivo
        if problem.isGoalState(current_state):
            return actions
            
        # Expandir el estado actual
        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_actions = actions + [action]
                new_cost = total_cost + step_cost
                priority_queue.push((successor, new_actions, new_cost), new_cost)
    
    # Si no se encuentra solución
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # Usar una cola de prioridad (PriorityQueue) para A*
    from util import PriorityQueue
    
    # Inicializar la cola de prioridad con el estado inicial
    # Cada elemento es una tupla (estado, lista_de_acciones, costo_acumulado)
    # La prioridad es f(n) = g(n) + h(n) donde g(n) es el costo y h(n) la heurística
    priority_queue = PriorityQueue()
    start_state = problem.getStartState()
    start_heuristic = heuristic(start_state, problem)
    priority_queue.push((start_state, [], 0), start_heuristic)
    
    # Conjunto para llevar registro de estados visitados
    visited = set()
    
    while not priority_queue.isEmpty():
        current_state, actions, total_cost = priority_queue.pop()
        
        # Si ya visitamos este estado, continuamos
        if current_state in visited:
            continue
            
        # Marcar el estado actual como visitado
        visited.add(current_state)
        
        # Verificar si hemos llegado al objetivo
        if problem.isGoalState(current_state):
            return actions
            
        # Expandir el estado actual
        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_actions = actions + [action]
                new_cost = total_cost + step_cost
                # Calcular f(n) = g(n) + h(n)
                h_cost = heuristic(successor, problem)
                f_cost = new_cost + h_cost
                priority_queue.push((successor, new_actions, new_cost), f_cost)
    
    # Si no se encuentra solución
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
