# Write a python program to implement the Iterative Deepening Search (IDS) algorithm.
def dls(graph, current_node, goal_node, limit, path, visited):
    visited.add(current_node)
    path.append(current_node)
    if current_node == goal_node:
        return path
    if limit <= 0:
        path.pop()
        return None
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            result = dls(graph, neighbor, goal_node, limit - 1, path, visited)
            if result is not None:
                return result
    path.pop()
    return None
def iterative_deepening_search(graph, start_node, goal_node, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit: {depth}")
        visited = set()
        path = []
        result = dls(graph, start_node, goal_node, depth, path, visited)
        if result is not None:
            print("IDS Path Found:", result)
            return result
    print(f"No path found within depth {max_depth}.")
    return None
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
max_depth = 5
iterative_deepening_search(graph, start, goal, max_depth)