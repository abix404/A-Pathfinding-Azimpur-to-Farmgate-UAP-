"""
© 2025 Bokhtear MD Abid | University of Asia Pacific
A* search from Home to UAP on a custom Dhaka map
Run to see optimal path and total cost.
"""

from collections import defaultdict
import math

h = {'Home': 3.07, 'BGB 1no Gate': 3.4, 
     'Azimpur Bus Stand': 3.12, 'Polashi Mor': 3.03, 
     'Fuller Road': 2.92, 'Shahid Minar Road': 3.05, 
     'Raju Memorial Sculpture': 2.56, 'Mukti Toron Circle': 2.45, 
     'Nilket Mor': 2.52, 'Sher-E-Bangla Road': 3.15, 'Shahbag Square': 1.97, 
     'Glass Factory': 3.04, 'Kataban Mor': 1.78, 'Bata Signal': 1.73, 
     'Science Lab': 1.87, 'BTCL Mor': 1.68, 'Zigatola Bus Stand': 2.22, 
     'DMD Road 5': 1.5, 'DMD Eidgah Road': 2.06, 'DMD 8no Bridge': 1.5, 
     'DMD Road 8': 1.27, 'Karwan Bazar': 0.68, 'Panthapath Mor': 0.46, 'Kolabagan': 1.17, 'UAP': 0.0}

edges = [('Home', 'Nilket Mor', 0.9), ('Home', 'BGB 1no Gate', 0.8), 
         ('Home', 'Azimpur Bus Stand', 0.8), ('Nilket Mor', 'Science Lab', 0.55), 
         ('Nilket Mor', 'Mukti Toron Circle', 0.2), ('Nilket Mor', 'Azimpur Bus Stand', 0.55), 
         ('Azimpur Bus Stand', 'Polashi Mor', 0.4), ('Polashi Mor', 'Fuller Road', 0.23), 
         ('Fuller Road', 'Shahid Minar Road', 0.33), ('Shahid Minar Road', 'Raju Memorial Sculpture', 0.7), 
         ('Raju Memorial Sculpture', 'Shahbag Square', 0.65), ('Shahbag Square', 'Karwan Bazar', 1.4), 
         ('Karwan Bazar', 'UAP', 0.9), ('Polashi Mor', 'Mukti Toron Circle', 0.75), 
         ('Mukti Toron Circle', 'Kataban Mor', 0.8), ('Kataban Mor', 'Shahbag Square', 0.5), 
         ('Kataban Mor', 'Bata Signal', 0.25), ('Kataban Mor', 'Karwan Bazar', 1.3), 
         ('Karwan Bazar', 'Panthapath Mor', 0.58), ('Panthapath Mor', 'UAP', 0.47), 
         ('Bata Signal', 'Science Lab', 0.55), ('Bata Signal', 'Karwan Bazar', 1.41), 
         ('Science Lab', 'Panthapath Mor', 1.6), ('Science Lab', 'BTCL Mor', 0.2), 
         ('BTCL Mor', 'DMD Road 5', 0.3), ('DMD Road 5', 'DMD Road 8', 0.5), 
         ('DMD Road 8', 'Panthapath Mor', 0.95), ('BGB 1no Gate', 'Sher-E-Bangla Road', 1.05), 
         ('Sher-E-Bangla Road', 'Glass Factory', 0.35), ('Glass Factory', 'Zigatola Bus Stand', 1.2), 
         ('Zigatola Bus Stand', 'DMD Eidgah Road', 0.55), ('DMD Eidgah Road', 'DMD 8no Bridge', 0.75), 
         ('DMD 8no Bridge', 'Kolabagan', 0.8), ('Kolabagan', 'Panthapath Mor', 1.0), 
         ('Zigatola Bus Stand', 'Science Lab', 0.8), ('DMD 8no Bridge', 'DMD Road 5', 0.8)]

graph = defaultdict(list)
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

def astar(start="Home", goal="UAP"):
    open_set = {start}  # Fixed: Changed from {{start}} to {start}
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0.0
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = h[start]
    closed_set = set()
    
    while open_set:
        current = min(open_set, key=lambda n: f_score[n])
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]
        
        open_set.remove(current)
        closed_set.add(current)
        
        for neighbor, w in graph[current]:
            if neighbor in closed_set: 
                continue
            tentative_g = g_score[current] + w
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                open_set.add(neighbor)
    
    return None, math.inf

if __name__ == "__main__":
    path, cost = astar()
    if path:
        print("Optimal path:", " -> ".join(path))
        print("Optimal cost (km):", round(cost, 3))
    else:
        print("No path found from Home to UAP")