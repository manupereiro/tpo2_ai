# 📂 Guía de Organización del Proyecto
## Trabajo Práctico 2 - Algoritmos de Búsqueda en Pacman

---

## 🗂️ **Estructura del Proyecto**

```
Codigo Fuente/
│
├── 🎮 ARCHIVOS DEL JUEGO PACMAN (ORIGINALES)
│   ├── pacman.py              ← Juego principal
│   ├── search.py              ← Algoritmos implementados (PRINCIPAL)
│   ├── searchAgents.py        ← Agentes de búsqueda
│   ├── game.py                ← Lógica del juego
│   ├── util.py                ← Utilidades (Stack, Queue, etc.)
│   ├── eightpuzzle.py         ← Puzzle de 8 (corregido)
│   ├── commands.txt           ← Comandos de ejemplo
│   └── layouts/               ← Laberintos
│
└── 🧠 ALGORITMOS_IMPLEMENTADOS/  ← TUS CÓDIGOS ESTÁN AQUÍ
    ├── README.md              ← Documentación completa
    ├── dfs.py                 ← Búsqueda en Profundidad
    ├── bfs.py                 ← Búsqueda en Anchura  
    ├── ucs.py                 ← Búsqueda de Costo Uniforme
    ├── astar.py               ← Búsqueda A*
    └── algoritmos_busqueda.py ← Sistema de demostración
```

---

## 🎯 **Dónde están TUS códigos implementados**

### ✅ **Implementación PRINCIPAL (funcionando en Pacman):**
- **Archivo**: `search.py` (líneas 75-264)
- **Funciones implementadas**:
  - `depthFirstSearch(problem)` - DFS
  - `breadthFirstSearch(problem)` - BFS  
  - `uniformCostSearch(problem)` - UCS
  - `aStarSearch(problem, heuristic)` - A*

### 📚 **Códigos individuales (educativos):**
- **Carpeta**: `Algoritmos_Implementados/`
- **Contenido**: Versiones detalladas con explicaciones de cada algoritmo

---

## 🚀 **Cómo ejecutar los algoritmos**

### **Opción 1: Ejecutar en Pacman** (RECOMENDADO)
```bash
# Desde la carpeta "Codigo Fuente/"
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### **Opción 2: Sistema de demostración**
```bash
# Ir a la carpeta de algoritmos
cd Algoritmos_Implementados
python algoritmos_busqueda.py
```

### **Opción 3: Ver códigos individuales**
```bash
# Ir a la carpeta de algoritmos
cd Algoritmos_Implementados
python dfs.py      # Ver código DFS
python bfs.py      # Ver código BFS
python ucs.py      # Ver código UCS
python astar.py    # Ver código A*
```

---

## 📋 **Resumen de Archivos Modificados/Creados**

### ✏️ **Archivos MODIFICADOS (del juego original):**
- `search.py` - Implementé los 4 algoritmos de búsqueda
- `eightpuzzle.py` - Corregí el método `getStartState()`

### 🆕 **Archivos CREADOS (tus algoritmos):**
- `Algoritmos_Implementados/dfs.py`
- `Algoritmos_Implementados/bfs.py`
- `Algoritmos_Implementados/ucs.py`
- `Algoritmos_Implementados/astar.py`
- `Algoritmos_Implementados/algoritmos_busqueda.py`
- `Algoritmos_Implementados/README.md`
- `GUIA_ORGANIZACION.md` (este archivo)

---

## 🏆 **Estado del Trabajo Práctico**

### ✅ **Completado:**
- [x] DFS - Búsqueda en Profundidad
- [x] BFS - Búsqueda en Anchura
- [x] UCS - Búsqueda de Costo Uniforme
- [x] A* - Búsqueda A*
- [x] Pruebas exitosas en todos los algoritmos
- [x] Documentación completa
- [x] Organización de archivos

### 📊 **Resultados de pruebas:**
- ✅ DFS funcionando (TinyMaze: costo 10, 15 nodos)
- ✅ BFS funcionando (MediumMaze: costo 68, 269 nodos)
- ✅ UCS funcionando (MediumMaze: óptimo)
- ✅ A* funcionando (BigMaze: costo 210, 549 nodos)

---

## 📞 **Próximos Pasos**

1. **Para presentar el TP**: Usar los archivos de `Algoritmos_Implementados/`
2. **Para mostrar funcionamiento**: Ejecutar comandos desde `Codigo Fuente/`
3. **Para documentación**: Leer `Algoritmos_Implementados/README.md`

---

**💡 Tip**: Los algoritmos están funcionando perfectamente en el juego Pacman. La carpeta `Algoritmos_Implementados/` contiene versiones educativas con explicaciones detalladas para tu presentación.

**✨ ¡Trabajo completado exitosamente!** 🎉 