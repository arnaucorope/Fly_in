from collections import deque
from graph.hub import Hub
from graph.connection import Connection

class Pathfinder:
    def __init__(self, graph: dict[Hub, list[Connection]]) -> None:
        self.graph = graph

    def find_route_bfs(self) -> list[Hub]:
        for hub in self.graph:
            if hub.type == "start_hub":
                start = hub
            elif hub.type == "end_hub":
                end = hub
        queue = deque([start])
        visited = [start]
        parents = {}

        while queue:
            current = queue.popleft()
            for connection in self.graph[current]:
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
