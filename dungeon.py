# TODO: PRIORITY QUEUE NOT CONNECTED WITH GRID. NEED TO REHEAP AFTER CHOOSING TILE

from enum import Enum, auto
from pqueue import PQueue
import random

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
        return self.__str__()
    def __str__(self) -> str:
        return str(self.value)


class Rooms(Enum):
    START = room(1, 3, 3, 0b0010)
    hallway_VERT = room(2, 3, 5, 0b0011)
    hallway_HORIZ = room(3, 5, 3, 0b1100)
    intersection = room(4, 3, 3, 0b1111)
    l_cap = room(5, 3, 3, 0b0100)
    r_cap = room(6, 3, 3, 0b1000)
    u_cap = room(7, 3, 3, 0b0001)
    d_cap = room(8, 3, 3, 0b0010)


class Dungeon():
    size: int
    grid: list

    def __init__(self, size = 10) -> None:
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.grid[size // 2][size // 2] = Rooms.START
        max_rooms = 10
        
        # generate dungeon using wave function collapse
        queue = PQueue([(size//2-1, size//2, [r for r in Rooms if r.value.doors & 0b0001])], lambda o: len(o[2]))
        for _ in range(10):
            if len(queue.elems) == 0: break
            r = queue.pop()
            if len(r[2]) == 1:
                self.grid[r[0]][r[1]] = r[2][0]
            else:
                self.grid[r[0]][r[1]] = random.choice(r[2])
            
            y,x = r[0], r[1]

            if x > 0 and self.grid[y][x-1] is None:
                queue.add_elem((y, x-1, self.filter_tile(y,x-1)))
            if y > 0 and self.grid[y-1][x] is None:
                queue.add_elem((y-1, x, self.filter_tile(y-1,x)))
            if x < size-1 and self.grid[y][x+1] is None:
                queue.add_elem((y, x+1, self.filter_tile(y,x+1)))
            if y < size-1 and self.grid[y+1][x] is None:
                queue.add_elem((y+1, x, self.filter_tile(y+1,x)))
            
            print(self)
            input()
    
    def filter_tile(self, r, c):
        p = [r for r in Rooms if r.value != 1]
        
        if c > 0:
            if self.grid[r][c-1] is not None:
                if ~(self.grid[r][c-1].value.doors & 0b0100):
                    p = [x for x in p if x.value.doors & 0b1000]
        if r > 0:
            if self.grid[r-1][c] is not None:
                if ~(self.grid[r-1][c].value.doors & 0b0001):
                    p = [x for x in p if x.value.doors & 0b0010]
        if c < self.size-1:
            if self.grid[r][c+1] is not None:
                if ~(self.grid[r][c+1].value.doors & 0b1000):
                    p = [x for x in p if x.value.doors & 0b0100]
        if r < self.size-1:
            if self.grid[r+1][c] is not None:
                if ~(self.grid[r+1][c].value.doors & 0b0010):
                    p = [x for x in p if x.value.doors & 0b0001]

        return p

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
