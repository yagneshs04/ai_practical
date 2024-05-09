import heapq

def best_first_search(graph, start, goal):
    explored, frontier = set(), [(0, start)]
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: return True
        explored.add(current)
        [heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor)) for neighbor in graph[current] if neighbor not in explored]
    return False

def heuristic(node, goal): return 0

# Example usage:
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
start_node, goal_node = 'A', 'F'
print(best_first_search(graph, start_node, goal_node))
