import Exception

class MapError(Exception):
    @staticmethod
    def from_file(error: OSError | UnicodeError, file: str) -> "MapError":
        if isinstance(error, OSError):
            return MapError(f"Could not read file: {file}")
        return MapError(f"File is not valid UTF-8 text: {file}")

    @staticmethod
    def from_lark(error: UnexpectedInput, map_text: str) -> "MapError":

