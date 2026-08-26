class Dungeon():
    size: int
    grid: list

    def __init__(self, size = 5) -> None:
        self.grid = [[None for _ in range(size)] for _ in range(size)]

        # generate dungeon using wave function collapse

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        o = ""
        for y in self.grid:
            for x in y:
                o += ". "
            o += "\n"
        return o

