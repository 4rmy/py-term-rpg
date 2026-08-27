from enum import Enum, auto

class room():
    value: int
    width: int
    height: int
    doors: int # 0b(left)(right)(up)(down)

    def __init__(self, value: int, width: int, height: int, doors: int) -> None:
        self.value = value
        self.width = width
        self.height = height
        self.doors = doors

    def __repr__(self) -> str:
        return self.str()
    def __str__(self) -> str:
        return str(self.value)



START = room(1, 3, 3, 0b0010)

class Rooms(Enum):
    hallway_VERT = room(2, 3, 5, 0b0011)
    hallway_HORIZ = room(3, 5, 3, 0b1100)
    intersection = room(4, 3, 3, 0b1111)
    l_cap = room(5, 3, 3, 0b0100)
    r_cap = room(6, 3, 3, 0b1000)
    u_cap = room(5, 3, 3, 0b0001)
    d_cap = room(6, 3, 3, 0b0010)


class Dungeon():
    size: int
    grid: list

    def __init__(self, size = 10) -> None:
        self.grid = [[None for _ in range(size)] for _ in range(size)]

        self.grid[size-2][size // 2] = START

        # generate dungeon using wave function collapse

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        o = ""
        for y in self.grid:
            for x in y:
                o += (str(x.value) + " ") if x else ". "
            o += "\n"
        return o

__all__ = ["Dungeon"]

if __name__ == "__main__":
    print(Dungeon())
