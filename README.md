# A* Pathfinding Project: Optimal Route from Azimpur to Farmgate (UAP)

## Overview
This project implements the **A\*** search algorithm to find the shortest path from **Azimpur (Home)** to **Farmgate (UAP)** in a directed, weighted graph representing a segment of Dhaka city's road network.  
The algorithm uses **real-world travel distances** as edge weights and **Euclidean straight-line distances** as heuristic values to guide the search.  

The project outputs include:
- The **optimal path**
- **Search tree**
- **Iteration table**
- **Heuristic consistency analysis**

---

## Problem Description
The goal is to compute the **shortest path** from a starting location (**Azimpur / Home**) to a destination (**Farmgate / UAP**) using the **A\*** search algorithm.  

- **Graph model:** Portion of Dhaka’s road network  
- **Nodes:** Key locations  
- **Edges:** Directed travel paths with real distances (km)  
- **Heuristic:** Straight-line distance from each node to UAP  

---

## Objectives
- Apply the A\* search algorithm to find the **optimal path with minimal travel cost**.  
- Ensure the heuristic is **admissible** and analyze **consistency**.  
- Provide a detailed trace of the search process, including:
  - ✅ Optimal path and total cost  
  - ✅ Search tree of explored states  
  - ✅ Iteration table showing algorithm’s progress  
  - ✅ Heuristic consistency check  

---

## Graph Representation
- **Nodes:** Real-world locations (Azimpur, Nilket Mor, Science Lab, UAP, etc.)  
- **Edges:** Directed travel distances (km)  
- **Heuristics:** Euclidean distances to UAP (admissible estimates)  

---

## Constraints
- Directed graph: only valid edge directions allowed  
- Non-negative edge costs: suitable for A\* / Dijkstra  
- Heuristics must be:
  - **Admissible:** `h(n) ≤ h*(n)`  
  - **Consistent:** `h(u) - h(v) ≤ c(u,v)`  

---

## Approach
**A\* Algorithm Implementation**
- Evaluation function:  

f(n) = g(n) + h(n)
- `g(n)`: Actual cost from start to node n  
- `h(n)`: Heuristic estimate from node n to goal  

- Maintains:
- **Open List** (frontier)  
- **Closed List** (expanded nodes)  

- Expands the node with the **lowest f(n)** at each step  

**Outputs Generated:**
- ✅ Optimal path:  
Home → Nilket Mor → Science Lab → Panthapath Mor → UAP
Cost = 3.52 km

- ✅ Search tree  
- ✅ Iteration table (g, h, f, Open, Closed)  
- ✅ Heuristic consistency table  

---

## Results
- **Optimal Path:**  
`Home → Nilket Mor → Science Lab → Panthapath Mor → UAP`  
**Total Cost = 3.52 km**

- **Heuristic Analysis:**
- ✅ Admissible → holds for all nodes  
- ⚠️ Consistency → violated for edge **Nilket Mor → Science Lab**, but admissibility still guarantees optimality  

- **Outputs Produced:**
- Search tree (explored paths)  
- Iteration trace table  
- Consistency validation table  

---

## Installation and Usage

### Prerequisites
- Python **3.x**  
- Text editor / IDE (VS Code, PyCharm, etc.)  
- Document viewer (MS Word for report)  

### Steps
```bash
# Clone the repository
git clone https://github.com/<your-username>/astar-pathfinding-dhaka.git
cd astar-pathfinding-dhaka

# Run the algorithm
python src/astar_pathfinding.py
Ensure graph data (nodes, edges, heuristics) matches the report’s tables
View results in docs/ for detailed explanations and diagrams
```
Conclusion

The A* algorithm successfully computed the optimal route from Azimpur to Farmgate (UAP) with a cost of 3.52 km.

The heuristic was admissible, guaranteeing optimality

One edge violated consistency, but the solution remained optimal

The project provides:

Iteration tables

Search trees

Heuristic validation

Demonstrating A*’s effectiveness in real-world navigation problems.
