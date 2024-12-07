# Búsqueda de Caminos en Grafos

Este repositorio implementa y compara varios algoritmos de búsqueda en grafos para la resolución de problemas de caminos. Los algoritmos incluidos son:

- **Búsqueda por anchura (BFS)**  
- **Búsqueda en profundidad (DFS)**  
- **Búsqueda por ramificación y acotación**  
- **Búsqueda por ramificación y acotación con subestimación**  

## 📋 Descripción

La búsqueda de caminos en grafos es una técnica fundamental en la computación y las ciencias aplicadas. Este proyecto explora distintas estrategias para encontrar soluciones óptimas (o aproximadas) en diferentes tipos de grafos. Los algoritmos se implementan de manera estructurada y se incluyen ejemplos de uso y análisis de rendimiento.

## 🚀 Algoritmos Implementados

1. **Búsqueda por anchura (BFS):**  
   Explora todos los nodos a una profundidad dada antes de pasar a la siguiente profundidad. Garantiza encontrar el camino más corto en grafos no ponderados.

2. **Búsqueda en profundidad (DFS):**  
   Sigue un camino hasta el final antes de retroceder y explorar rutas alternativas. Ideal para explorar exhaustivamente un grafo.

3. **Búsqueda por ramificación y acotación:**  
   Evalúa las opciones disponibles utilizando una estrategia de cola de prioridad. Reduce el espacio de búsqueda eliminando caminos subóptimos.

4. **Búsqueda por ramificación y acotación con subestimación:**  
   Utiliza una función heurística para priorizar los nodos más prometedores, acelerando la búsqueda en problemas donde se puede estimar el costo restante.

## 📦 Estructura del Proyecto

```plaintext
📁 Algoritmos-de-busquedad-en-grafos/
    ├── run.py           # Ejecución del los algoritmos
    ├── search.py        # Implementación de DFS, BFS, ramificación y acotación, ramificación y acotación con subestimación 
    ├── utils.py         # Clases y funciones necesarias para ejecutar el código 
├── README.md            # Este archivo
