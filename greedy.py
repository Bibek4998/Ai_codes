# Wrrite a python program to implement Greedy Best First Search algorithm.
import heapq
def greedy_best_first_search(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristics[start], [start]))  # (h(n), path)
    visited = set()
    while open_set:
        h, path = heapq.heappop(open_set)
        current = path[-1]

        if current == goal:
            print("Greedy Path Found:", path)
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristics.get(neighbor, float('inf')), path + [neighbor]))

    print("No path found.")
    return []
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
heuristics = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}
start = 'A'
goal = 'F'
greedy_best_first_search(graph, heuristics, start, goal)