A* Pathfinding Project: Optimal Route from Azimpur to Farmgate (UAP)
Overview
This project implements the A* search algorithm to find the shortest path from Azimpur (Home) to Farmgate (UAP) in a directed, weighted graph representing a segment of Dhaka city's road network. The algorithm uses real-world travel distances as edge weights and Euclidean straight-line distances as heuristic values to guide the search. The project includes detailed outputs such as the optimal path, search tree, iteration table, and heuristic consistency analysis.
Problem Description
The goal is to compute the shortest path from a starting location (Azimpur, referred to as "Home") to a destination (Farmgate, referred to as "UAP") using the A* search algorithm. The graph models a portion of Dhaka’s road network, with nodes representing key locations, directed edges indicating valid travel directions, and edge weights representing travel distances in kilometers. Heuristic values estimate the straight-line distance from each node to the goal (UAP).
Objectives

Apply the A* search algorithm to find the optimal path with minimal travel cost.
Ensure the heuristic is admissible (never overestimates true cost) and analyze its consistency.
Provide a detailed trace of the search process, including:
Optimal path and its total cost.
Search tree of explored states.
Iteration table showing the algorithm’s progress.
Heuristic consistency check for all edges.



Graph Representation

Nodes: Represent real-world locations (e.g., Azimpur, Nilket Mor, Science Lab, UAP).
Edges: Directed connections between locations, indicating valid travel directions.
Edge Weights: Travel distances in kilometers.
Heuristic Values: Euclidean (straight-line) distances from each node to UAP.

Constraints

The graph is directed, allowing movement only along specified edge directions.
Edge costs are non-negative, making A* and Dijkstra’s algorithms suitable.
Heuristics must be:
Admissible: Never overestimate the true cost to the goal.
Consistent: Satisfy the triangle inequality for all edges (h(u) - h(v) ≤ c(u,v)).



Approach

A Algorithm Implementation*:
Uses the evaluation function: f(n) = g(n) + h(n), where:
g(n): Actual cost from the start node to node n.
h(n): Heuristic estimate from node n to the goal.


Maintains an Open List (frontier) and Closed List (expanded nodes).
Expands the node with the lowest f(n) at each step.


Outputs:
Optimal path from Home to UAP with total travel cost.
Search tree visualizing explored states.
Iteration table detailing each step (path, g(n), h(n), f(n), Open List, Closed List).
Heuristic consistency check table for all edges.



Results

Optimal Path: Home → Nilket Mor → Science Lab → Panthapath Mor → UAP (total cost: 3.52 km).
Heuristic Analysis:
Admissibility: Confirmed for all nodes, as h(n) ≤ h*(n) (heuristic never overestimates true cost).
Consistency: Not fully satisfied due to the edge "Nilket Mor to Science Lab" violating the condition (h(u) - h(v) > c(u,v)). However, admissibility ensures optimality.


Outputs Generated:
Search tree illustrating explored paths.
Iteration table tracing the A* algorithm’s progress.
Consistency table validating heuristic properties.



Files

Report - Optimal Pathfinding Using A Search and Real Map Heuristics.docx: Detailed report containing:
Problem description, graph representation, and constraints.
A* algorithm explanation and outputs (path, search tree, iteration table).
Heuristic admissibility and consistency analysis.
Visualizations (map, search tree, etc.).


image1.png, image2.jpg, image3.jpg, image4.png, image5.png, image6.png: Supporting images for the map, search tree, and other visualizations.
Code: Python implementation of the A* algorithm (included in the report).

How to Run

Prerequisites:
Python 3.x for running the A* algorithm code.
A text editor or IDE to view/edit the code.
A document viewer (e.g., Microsoft Word) to access the report.


Steps:
Open the Python code provided in the report.
Ensure the graph data (nodes, edges, weights, heuristics) is correctly defined as per the report’s path cost and heuristic tables.
Run the Python script to execute the A* algorithm and generate the optimal path, iteration table, and other outputs.
Refer to the report for detailed explanations and visualizations.



Conclusion
The A* search algorithm successfully identified the optimal route from Azimpur (Home) to Farmgate (UAP) with a total cost of 3.52 km. The heuristic was admissible, ensuring optimality, though it was not fully consistent due to one edge violation. The project provides a comprehensive analysis of the search process through iteration tables, search trees, and heuristic validation, demonstrating the effectiveness of A* for real-world navigation problems.
