# 🧠 Algoritmos de Búsqueda Implementados
## Trabajo Práctico 2 - Inteligencia Artificial

Esta carpeta contiene las implementaciones individuales de los algoritmos de búsqueda para el juego Pacman.

---

## 📁 **Contenido de la Carpeta**

### 🔍 **Algoritmos Individuales**

| Archivo | Algoritmo | Descripción |
|---------|-----------|-------------|
| **`dfs.py`** | Depth-First Search | Búsqueda en Profundidad |
| **`bfs.py`** | Breadth-First Search | Búsqueda en Anchura |
| **`ucs.py`** | Uniform Cost Search | Búsqueda de Costo Uniforme |
| **`astar.py`** | A-Star Search | Búsqueda A* |

### 🎮 **Sistema de Demostración**

| Archivo | Descripción |
|---------|-------------|
| **`algoritmos_busqueda.py`** | Menú interactivo para probar todos los algoritmos |

---

## 🚀 **Cómo usar los códigos**

### **Opción 1: Ejecutar algoritmos individualmente**
```bash
# Ver explicación de cada algoritmo
python dfs.py
python bfs.py
python ucs.py
python astar.py
```

### **Opción 2: Usar el sistema de demostración**
```bash
python algoritmos_busqueda.py
```

### **Opción 3: Ejecutar en Pacman** (desde la carpeta padre)
```bash
# Volver a la carpeta principal
cd ..

# Ejecutar algoritmos en Pacman
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

---

## 📊 **Características de cada Algoritmo**

### 🌊 **DFS (Depth-First Search)**
- **Estructura**: Pila (LIFO)
- **Estrategia**: Profundidad primero
- **Optimalidad**: ❌ No garantiza solución óptima
- **Complejidad**: O(b^m)
- **Ventaja**: Usa menos memoria

### 🌀 **BFS (Breadth-First Search)**
- **Estructura**: Cola (FIFO)
- **Estrategia**: Nivel por nivel
- **Optimalidad**: ✅ Solución óptima (costos uniformes)
- **Complejidad**: O(b^d)
- **Ventaja**: Encuentra camino más corto

### 💰 **UCS (Uniform Cost Search)**
- **Estructura**: Cola de prioridad (por costo)
- **Estrategia**: Menor costo primero
- **Optimalidad**: ✅ Solución óptima
- **Complejidad**: O(b^(C*/ε))
- **Ventaja**: Maneja costos variables

### ⭐ **A* (A-Star Search)**
- **Estructura**: Cola de prioridad (por f(n) = g(n) + h(n))
- **Estrategia**: Combina costo + heurística
- **Optimalidad**: ✅ Solución óptima (heurística admisible)
- **Complejidad**: Depende de la heurística
- **Ventaja**: Más eficiente con buena heurística

---

## 🎯 **Comandos de Prueba Recomendados**

```bash
# Comparar algoritmos en el mismo laberinto
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs     # DFS
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs     # BFS
python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs     # UCS
python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic  # A*

# Probar en laberintos más grandes
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=bfs    # BFS en laberinto grande
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic  # A* en laberinto grande
```

---

## 📝 **Notas Importantes**

1. **Los algoritmos principales están implementados en**: `../search.py`
2. **Los archivos de esta carpeta son**: Versiones educativas con explicaciones detalladas
3. **Para ejecutar en Pacman**: Usar los comandos desde la carpeta padre (`Codigo Fuente/`)
4. **Estructura del proyecto**:
   ```
   Codigo Fuente/
   ├── Algoritmos_Implementados/    ← Estás aquí
   │   ├── dfs.py
   │   ├── bfs.py
   │   ├── ucs.py
   │   ├── astar.py
   │   ├── algoritmos_busqueda.py
   │   └── README.md
   ├── search.py                    ← Implementación principal
   ├── pacman.py                    ← Juego principal
   └── ... (otros archivos del juego)
   ```

---

## 🏆 **Resultados de Pruebas**

| Algoritmo | Laberinto | Costo | Nodos Expandidos | Tiempo |
|-----------|-----------|-------|------------------|--------|
| DFS | TinyMaze | 10 | 15 | 0.0s |
| BFS | TinyMaze | 8 | 15 | 0.0s |
| UCS | TinyMaze | 8 | 15 | 0.0s |
| A* | TinyMaze | 8 | 14 | 0.0s |
| BFS | MediumMaze | 68 | 269 | 0.0s |
| A* | BigMaze | 210 | 549 | 0.0s |

---

**📧 Contacto**: Para preguntas sobre la implementación, consultar con el equipo de desarrollo.

**📅 Fecha**: Trabajo Práctico 2 - Inteligencia Artificial

**✨ Estado**: ✅ Completado y Probado 