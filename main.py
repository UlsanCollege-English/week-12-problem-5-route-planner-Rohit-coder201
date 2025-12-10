import heapq
from collections import deque


def route_planner(graph, start, goal, weighted):
    """
    Plan a route between start and goal.

    If weighted is False:
        - graph: dict node -> list of neighbor nodes (unweighted).
        - Use BFS to find a path with the fewest edges.
        - Return (path, steps) where steps = number of edges.

    If weighted is True:
        - graph: dict node -> list of (neighbor, weight) pairs (positive weights).
        - Use Dijkstra to find a path with the smallest total weight.
        - Return (path, total_cost).

    In both cases:
        - If start or goal not in graph, or no path exists, return ([], None).
    """
    # TODO Step 1–3: Understand the two modes and write down inputs/outputs.
    # TODO Step 4: Plan how to choose BFS or Dijkstra based on the `weighted` flag.
    # TODO Step 5: Write pseudocode for the BFS branch and the Dijkstra branch.
    # TODO Step 6: Implement helper functions (if you wish) and call them here.
    # TODO Step 7: Test both unweighted and weighted graphs, including no-path cases.
    # TODO Step 8: Reflect why BFS is used for unweighted and Dijkstra for weighted.

    if start not in graph or goal not in graph:
        return [], None

    if start == goal:
        return [start], 0

    if not weighted:
        queue = deque([start])
        visited = {start}
        parent = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        if goal not in parent:
            return [], None

        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        cost = max(0, len(path) - 1)
        return path, cost

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {start: None}
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if node == goal:
            break
        if dist > distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if distances.get(goal, float('inf')) == float('inf'):
        return [], None

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path, distances[goal]


if __name__ == "__main__":
    pass
