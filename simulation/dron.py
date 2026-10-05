
def find_route(graph: dict[Hub, list[Connection]]) -> list[Hub]:
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
    path.append(end)
    current = parents[end]
    while True:
        current = parents[current]
        path.append(parents[current])
        if start in path:
            break


