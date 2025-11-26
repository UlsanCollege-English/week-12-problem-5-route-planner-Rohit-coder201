import heapq
from collections import deque


def route_planner(graph, start, goal, weighted):
    # if start or goal not in graph → fail early
    if start not in graph or goal not in graph:
        return [], None

    # Case 1: BFS for unweighted graph
    if not weighted:
        return bfs_path(graph, start, goal)

    # Case 2: Dijkstra for weighted graph
    return dijkstra_path(graph, start, goal)


def bfs_path(graph, start, goal):
    if start == goal:
        return [start], 0

    queue = deque([start])
    visited = {start: None}  # store parent for reconstruction

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)

                if neighbor == goal:
                    return build_path(visited, start, goal)

    return [], None  # no path


def dijkstra_path(graph, start, goal):
    if start == goal:
        return [start], 0

    pq = [(0, start)]  # (cost, node)
    visited_cost = {start: 0}
    parent = {start: None}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return build_path(parent, start, goal, cost)

        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            if neighbor not in visited_cost or new_cost < visited_cost[neighbor]:
                visited_cost[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    return [], None  # no path found


def build_path(parent, start, goal, cost=None):
    # Reconstruct path backwards
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    # Determine cost if BFS path
    if cost is None:
        cost = len(path) - 1

    return path, cost
