from graph.hub import Hub

class Connection:
    def __init__(
            self, 
            source: Hub, 
            target: Hub, 
            max_link_capacity: int
            ) -> None:
        self.source = source
        self.target = target
        self.max_link_capacity = max_link_capacity
