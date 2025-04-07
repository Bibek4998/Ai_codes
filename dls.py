# Write a python program to implement the Depth Limited Search (DLS) algorithm.
def depth_limited_search(graph, current_node, goal_node, limit, path=None, visited=None):
    if path is None:
        path = [current_node]
    if visited is None:
        visited = set()
    visited.add(current_node)
    if current_node == goal_node:
        print("DLS Path Found:", path)
        return path
    if limit <= 0:
        return None
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            new_path = list(path)
            new_path.append(neighbor)
            result = depth_limited_search(graph, neighbor, goal_node, limit - 1, new_path, visited)
            if result is not None:
                return result
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
depth_limit = 3
result = depth_limited_search(graph, start, goal, depth_limit)

if not result:
    print(f"No path found within depth limit {depth_limit}.")