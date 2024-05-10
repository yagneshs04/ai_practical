from collections import deque

def shortest_path(graph, start, end):
    visited, queue = set(), deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        if vertex == end:
            return path
        visited.add(vertex)
        queue.extend((n, path + [n]) for n in graph[vertex] if n not in visited)

city_network = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
start_city, end_city = 'B', 'F'

shortest_path = shortest_path(city_network, start_city, end_city)
print(f"Shortest path from {start_city} to {end_city}: {' -> '.join(shortest_path)}" 
      if shortest_path 
      else f"No path found from {start_city} to {end_city}")

