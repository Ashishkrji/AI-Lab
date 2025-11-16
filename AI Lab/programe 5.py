#Implementation of heuristic search techniques in Python.

import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {},
    'E': {'H': 2},
    'F': {},
    'H': {}
}

heuristic = {'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 2, 'F': 3, 'H': 0}

def a_star(start, goal):
    queue = [(heuristic[start], 0, [start])]  # (f, g, path)
    while queue:
        f, g, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, g
        for neigh, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + heuristic[neigh]
            heapq.heappush(queue, (new_f, new_g, path + [neigh]))

path, cost = a_star('A', 'H')
print("Path:", path, " Cost:", cost)
