# Write a python program to implement the Bidirectional Search algorithm.
from collections import deque
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    forward_queue = deque([[start]])
    backward_queue = deque([[goal]])
    forward_visited = {start: [start]}
    backward_visited = {goal: [goal]}
    while forward_queue and backward_queue:
        path_f = forward_queue.popleft()
        node_f = path_f[-1]
        for neighbor in graph.get(node_f, []):
            if neighbor not in forward_visited:
                new_path = path_f + [neighbor]
                forward_visited[neighbor] = new_path
                forward_queue.append(new_path)
                if neighbor in backward_visited:
                    full_path = new_path[:-1] + backward_visited[neighbor][::-1]
                    print("Bidirectional Path Found:", full_path)
                    return full_path
        path_b = backward_queue.popleft()
        node_b = path_b[-1]
        for neighbor in graph:
            if node_b in graph[neighbor]:
                if neighbor not in backward_visited:
                    new_path = path_b + [neighbor]
                    backward_visited[neighbor] = new_path
                    backward_queue.append(new_path)
                    if neighbor in forward_visited:
                        full_path = forward_visited[neighbor] + new_path[-2::-1]
                        print("Bidirectional Path Found:", full_path)
                        return full_path
    print("No path found.")
    return []
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = 'A'
goal = 'F'
bidirectional_search(graph, start, goal)