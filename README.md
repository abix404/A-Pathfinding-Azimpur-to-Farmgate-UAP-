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

## Repository Contents
