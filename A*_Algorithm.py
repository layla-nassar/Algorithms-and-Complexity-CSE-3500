import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []  # Priority queue: (f = g + h, g, node, path)
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))

    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g  # Found the shortest path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found
