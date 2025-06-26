# pacmanAgents.py
# ---------------
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


from pacman import Directions
from game import Agent
import random
import game
import util

class LeftTurnAgent(game.Agent):
    "An agent that turns left at every opportunity"

    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        current = state.getPacmanState().configuration.direction
        if current == Directions.STOP: current = Directions.NORTH
        left = Directions.LEFT[current]
        if left in legal: return left
        if current in legal: return current
        if Directions.RIGHT[current] in legal: return Directions.RIGHT[current]
        if Directions.LEFT[left] in legal: return Directions.LEFT[left]
        return Directions.STOP

class GreedyAgent(Agent):
    def __init__(self, evalFn="scoreEvaluation"):
        self.evaluationFunction = util.lookup(evalFn, globals())
        assert self.evaluationFunction != None

    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal: legal.remove(Directions.STOP)

        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.evaluationFunction(state), action) for state, action in successors]
        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        return random.choice(bestActions)

class SmartPacmanAgent(Agent):
    """
    Un agente inteligente que juega Pacman automáticamente, 
    evitando fantasmas y recolectando comida de manera eficiente.
    """
    
    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal: 
            legal.remove(Directions.STOP)
        
        if not legal:
            return Directions.STOP
            
        # Obtener información del estado actual
        pacmanPos = state.getPacmanPosition()
        food = state.getFood()
        ghosts = state.getGhostStates()
        ghostPositions = [ghost.getPosition() for ghost in ghosts]
        
        # Evaluar cada acción posible
        actionScores = []
        for action in legal:
            successor = state.generateSuccessor(0, action)
            score = self.evaluateAction(successor, action, pacmanPos, food, ghostPositions, ghosts)
            actionScores.append((score, action))
        
        # Elegir la mejor acción
        actionScores.sort(reverse=True)
        return actionScores[0][1]
    
    def evaluateAction(self, state, action, pacmanPos, food, ghostPositions, ghosts):
        """
        Evalúa qué tan buena es una acción considerando:
        - Distancia a fantasmas (evitar)
        - Distancia a comida (buscar)
        - Puntuación del estado resultante
        """
        newPos = state.getPacmanPosition()
        score = state.getScore()
        
        # Penalización por fantasmas cercanos
        ghostPenalty = 0
        for i, ghostPos in enumerate(ghostPositions):
            distance = self.manhattanDistance(newPos, ghostPos)
            if distance <= 1:
                # Muy peligroso estar tan cerca
                if ghosts[i].scaredTimer <= 0:
                    ghostPenalty -= 1000
                else:
                    # Si el fantasma está asustado, es bueno estar cerca
                    ghostPenalty += 200
            elif distance <= 3:
                # Moderadamente peligroso
                if ghosts[i].scaredTimer <= 0:
                    ghostPenalty -= 100 / distance
                else:
                    ghostPenalty += 50 / distance
        
        # Recompensa por comida cercana
        foodReward = 0
        foodList = food.asList()
        if foodList:
            closestFoodDist = min([self.manhattanDistance(newPos, foodPos) for foodPos in foodList])
            foodReward = 10.0 / (closestFoodDist + 1)
            
            # Recompensa extra por recoger comida
            if newPos in foodList:
                foodReward += 100
        
        # Recompensa por cápsulas de poder
        capsules = state.getCapsules()
        capsuleReward = 0
        if capsules:
            closestCapsuleDist = min([self.manhattanDistance(newPos, capsulePos) for capsulePos in capsules])
            capsuleReward = 20.0 / (closestCapsuleDist + 1)
            
            if newPos in capsules:
                capsuleReward += 200
        
        return score + ghostPenalty + foodReward + capsuleReward
    
    def manhattanDistance(self, pos1, pos2):
        """Calcula la distancia Manhattan entre dos posiciones"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def scoreEvaluation(state):
    return state.getScore()
