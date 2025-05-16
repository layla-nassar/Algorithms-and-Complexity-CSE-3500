def ida_star(graph, start, goal, heuristic):
    def dfs(path, g, threshold):
        current = path[-1]
        f = g + heuristic[current]
        if f > threshold:
            return f
        if current == goal:
            return path
        min_threshold = float('inf')
        for neighbor, weight in graph[current]:
            if neighbor not in path:
                new_path = path + [neighbor]
                t = dfs(new_path, g + weight, threshold)
                if isinstance(t, list):  # Found goal
                    return t
                if t < min_threshold:
                    min_threshold = t
        return min_threshold

    threshold = heuristic[start]
    path = [start]
    while True:
        result = dfs(path, 0, threshold)
        if isinstance(result, list):  # Path found
            cost = 0
            for i in range(len(result) - 1):
                for neighbor, weight in graph[result[i]]:
                    if neighbor == result[i + 1]:
                        cost += weight
                        break
            return result, cost
        if result == float('inf'):  # No solution
            return None, float('inf')
        threshold = result  # Update threshold and repeat
