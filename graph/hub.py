class Hub:
    def __init__(
            self,
            type: str,
            name: str,
            x: int,
            y: int,
            zone: str,
            color: str,
            max_drone: int,
            ) -> None:
        self.type = type
        self.name = name
        self.x = x
        self.y = y
        self.zone = zone
        self.color = color
        self.max_drone = max_drone
        self._n_drone = 0

    def set_n_drone(self, drones: int) -> None:
        self._n_drone += drones

    def get_n_drones(self) -> int:
        return self._n_drone

