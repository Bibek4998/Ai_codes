# Write a python program to implement the Breadth First Search (BFS) algorithm.
from collections import deque
def bfs(graph, start_node, goal_node):
    visited = set()
    queue = deque([[start_node]])
    if start_node == goal_node:
        print("Start is the goal!")
        return [start_node]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbors = graph.get(node, [])

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal_node:
                    print("BFS Path Found:", new_path)
                    return new_path
            visited.add(node)
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
bfs(graph, start, goal)
