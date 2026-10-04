from .hub import Hub
from .connection import Connection
from parser.models import MapModel

class Graph:
    def __init__(self, map_model: MapModel) -> None:
        self.map_model = map_model
        self.hubs: dict[str, Hub] = {}
        self.connections: list[Connection] = []
        self.adjacency: dict[Hub, list[Connection]] = {}

    def _create_hubs(self) -> None:
        for node_model in self.map_model.nodes:
            self.hubs[node_model.name] = Hub(
                    node_model.type,
                    node_model.name,
                    node_model.x,
                    node_model.y,
                    node_model.zone,
                    node_model.color,
                    node_model.max_drones,
                    )

    def _create_connections(self) -> None:
        for connection_model in self.map_model.connections:
            source = self.hubs[connection_model.source]
            target = self.hubs[connection_model.target]
            self.connections.append(Connection(
                source,
                target,
                connection_model.max_link_capacity
                ))

    def generate_graph(self) -> dict[Hub, list[Connection]]:
        self._create_hubs()
        self._create_connections()
        for hub in self.hubs.values():
            self.adjacency[hub] = []
        for connection in self.connections:
            self.adjacency[connection.source].append(connection)
            self.adjacency[connection.target].append(connection)
        return self.adjacency

