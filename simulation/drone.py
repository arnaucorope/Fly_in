from graph import Hub

class Drone:
    def __init__(self, drone_id: int, path: list[Hub]) -> None:
        self.id = drone_id
        self.path = path
        self._path_index = 0
        self.delivered = False

    def current_hub(self) -> Hub:
        return self.path[self._path_index]
    
    def next_hub(self) -> Hub | None:
        if self.delivered:
            return None
        return self.path[self._path_index + 1]

    def get_movement_info(self) -> dict:
        return {
            "drone": self,
            "current": self.current_hub(),
            "next": self.next_hub(),
            }

    def advance(self) -> None:
        if self.delivered:
            return
        self._path_index += 1
        if self._path_index == len(self.path) - 1:
            self.delivered = True
