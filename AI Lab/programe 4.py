#Implementation of uninformed search techniques in Python.

graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
def dfs(start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end =" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

print("BFS:"); bfs('A')
print("\nDFS:"); dfs('A')
    
            
