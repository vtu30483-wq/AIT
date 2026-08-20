import heapq
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}
def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node in visited:
            continue
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float("inf")
path, cost = a_star('A', 'D')
print("Optimal Path:", " -> ".join(path))
print("Total Travel Cost:", cost)
