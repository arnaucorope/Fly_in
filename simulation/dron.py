
def find_route_bfs(graph: dict[Hub, list[Connection]]) -> list[Hub]:
    for hub in graph:
        if hub.type == "start_hub":
            start = hub
        elif hub.type == "end_hub":
            end = hub
    queue = [start]
    visited = [start]
    parents = {}

    while queue:
        current = queue.popleft()
        for connection in graph[current]:
            if current == connection.target:
                neighbour = connection.source
            else:
                neighbour = connection.target
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                parents[neighbour] = current
        if end in parents:
            break
    path: list[Hub] = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(current)
    path.reverse()
    return path


def find_route_dfs(graph: dict[Hub, list[Connections]]) -> list[Hub]:
    for hub in graph:
        if hub.type == "start_hub":
            start = hub
        elif hub.type == "end_hub":
            end = hub

    visited = set()
    stack = []

    visited.add(start)
    stack.append(start)
    current = start
    while visited:
        for connection in graph[current]:
            if current == connection.source:
                neighbour = connection.target
            else:
                neighbour = connection.source
            if neighbour not in visited and neighbour == end:
                current = neighbour
                stack.append(current)
                visited.add(current)
                return stack
            elif neighbour not in visited:
                current = neighbour
                stack.append(current)
                visited.add(current)
            else:
                stack.pop(current)

    return stack



