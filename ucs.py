# Write a python program to implement the Uniform Cost Search (UCS) algorithm.
import heapq
def uniform_cost_search(graph, start_node, goal_node):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, [start_node]))  # (cost, path)
    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        if node == goal_node:
            print("UCS Path Found:", path)
            print("Total Cost:", cost)
            return path
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                total_cost = cost + edge_cost
                heapq.heappush(priority_queue, (total_cost, new_path))
    print("No path found.")
    return []
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
start = 'A'
goal = 'F'
uniform_cost_search(graph, start, goal)