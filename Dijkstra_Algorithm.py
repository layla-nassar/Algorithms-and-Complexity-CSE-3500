import heapq

def dijkstra(graph, start, goal):
    priority_queue = []  
    heapq.heappush(priority_queue, (0, start))  # (cost, node)

    came_from = {start: None}  # Stores the path
    cost_so_far = {start: 0}   # Stores the shortest distance to each node

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break  # Found the shortest path to goal

        for neighbor, edge_cost in graph.get(current_node, []):
            new_cost = current_cost + edge_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))
                came_from[neighbor] = current_node

    # Reconstruct the shortest path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from.get(node)

    return path[::-1], cost_so_far.get(goal, float('inf'))
