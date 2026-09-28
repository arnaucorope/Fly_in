from pathlib import Path
from lark import Lark, Tree
from lark.exceptions import UnexpectedInput
import sys


class MapParser:
    def __init__(self) -> None:
        grammar_path = Path(__file__).with_name("grammar.lark")
        self._parser = Lark.open(grammar_path)

    def read_file(self, file_route: str) -> str:
        try:
            with open(file_route, "r", encoding="utf-8") as file:
                text = file.read()
        except (OSError, UnicodeError):
            raise
        return text

    def parse_file(self, file_route: str) -> Tree:
        map_text = self.read_file(file_route)
        try:
            tree = self._parser.parse(map_text)
        except UnexpectedInput as error:
            raise
        return tree

    def convert_data(self, file_route: str) -> dict:
        tree = self.parse_file(file_route)
        branches = tree.children
        map_data = {}
        map_data["nodes"] = []
        map_data["connections"] = []
        for branch in branches:
            if branch.data == "count_drones":
                map_data["nb_drones"] = int(branch.children[0])
            elif branch.data in ("start_hub", "end_hub", "hub"):
                node_data = {
                        "type": str(branch.data),
                        "name": str(branch.children[0]),
                        "x": int(branch.children[1]),
                        "y": int(branch.children[2]),
                        }
                if len(branch.children) > 3:
                    data = branch.children[3]
                    metadata = data.children
                    for item in metadata:
                        if item.data == "color":
                            node_data["color"] = str(item.children[0])
                        elif item.data == "zone":
                            node_data["zone"] = str(item.children[0])
                        elif item.data == "max_drones":
                            node_data["max_drones"] = int(item.children[0])
                map_data["nodes"].append(node_data)
            elif branch.data == "connections":
                connection_data = {
                        "source": str(branch.children[0]),
                        "target": str(branch.children[1]),
                        }
                if len(branch.children) > 2:
                    data = branch.children[2]
                    metadata = data.children
                    connection_data["max_link_capacity"] = int(
                            metadata[0].children[0])
                map_data["connections"].append(connection_data)
        return map_data


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lark = MapParser()
        tree_lark = lark.convert_data(sys.argv[1])
        print(tree_lark)
