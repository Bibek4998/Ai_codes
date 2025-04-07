import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristics[start], 0, [start]))  # (f = g + h, g, path)
    visited = set()

    while open_set:
        f, g, path = heapq.heappop(open_set)
        current = path[-1]

        if current == goal:
            print("A* Path Found:", path)
            print("Total Cost:", g)
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics.get(neighbor, float('inf'))
                heapq.heappush(open_set, (new_f, new_g, path + [neighbor]))

    print("No path found.")
    return []

# Example graph (Adjacency list with costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristics (Estimated cost from node to goal 'F')
heuristics = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

# Example usage
start = 'A'
goal = 'F'
a_star_search(graph, heuristics, start, goal)
