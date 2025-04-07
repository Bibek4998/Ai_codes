# Write a python program to implement the Depth First Search (DFS) algorithm.
def dfs(graph, start_node, goal_node):
    visited = set()
    stack = [[start_node]]  
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal_node:
            print("DFS Path Found:", path)
            return path
        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            for neighbor in reversed(neighbors): 
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    print("No path found.")
    return []
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
goal = 'F'
dfs(graph, start, goal)