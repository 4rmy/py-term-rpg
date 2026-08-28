from pqueue import PQueue
from rooms import *
import random
from pprint import pprint
from os import system as call

# TEMP
def cls():
    call('cls')
# TEMP

class Dungeon():
    min_size: int
    max_size: int
    map: list

    def __init__(self, min_size = 5, max_size = 10) -> None:
        self.min_size = min_size
        self.max_size = max_size
        self.map = {(0,0): Rooms.START}

        # WFC impl
        queue = PQueue([(0,1,[r for r in Rooms.ALL() if r.value[1] & Directions.DOWN])], lambda o: len(o[2]))
        while queue and len(self.map) < max_size:
            # grab next tile
            tile = queue.pop()
            if (tile[0], tile[1]) in self.map: continue
            x,y = tile[0], tile[1]
            # collapse tile
            val = random.choice(tile[2])
            self.map[(x,y)] = val
            
            # re-evaluate tiles based on choice
            for i,v in enumerate(queue.elems):
                queue.elems[i] = (v[0],v[1], self.limitTile(v[0], v[1]))

            q = []
            # add next tiles
            if val.value[1] & Directions.UP and not (x,y+1) in self.map:
                q.append((x,y+1,self.limitTile(x,y+1)))
            if val.value[1] & Directions.DOWN and not (x,y-1) in self.map:
                q.append((x,y-1,self.limitTile(x,y-1)))
            if val.value[1] & Directions.LEFT and not (x-1,y) in self.map:
                q.append((x-1,y,self.limitTile(x-1,y)))
            if val.value[1] & Directions.RIGHT and not (x+1,y) in self.map:
                q.append((x+1,y,self.limitTile(x+1,y)))
            queue.add_elem(q)

            # find next priority
            queue.reheap()
        # TODO: cap off the map
    
    def limitTile(self, x, y):
        rooms = Rooms.ALL()
        if len(self.map) < self.min_size: rooms = [r for r in rooms if r not in [Rooms.UP_CAP, Rooms.DOWN_CAP, Rooms.LEFT_CAP, Rooms.RIGHT_CAP]]
        if (x,y-1) in self.map:
            if self.map[(x,y-1)].value[1] & Directions.UP:
                rooms = [r for r in rooms if r.value[1] & Directions.DOWN]
            else:
                rooms = [r for r in rooms if ~(r.value[1] & Directions.DOWN)]
        if (x,y+1) in self.map:
            if self.map[(x,y+1)].value[1] & Directions.DOWN:
                rooms = [r for r in rooms if r.value[1] & Directions.UP]
            else:
                rooms = [r for r in rooms if ~(r.value[1] & Directions.UP)]
        if (x-1,y) in self.map:
            if self.map[(x-1,y)].value[1] & Directions.RIGHT:
                rooms = [r for r in rooms if r.value[1] & Directions.LEFT]
            else:
                rooms = [r for r in rooms if ~(r.value[1] & Directions.LEFT)]
        if (x+1,y) in self.map:
            if self.map[(x+1,y)].value[1] & Directions.LEFT:
                rooms = [r for r in rooms if r.value[1] & Directions.RIGHT]
            else:
                rooms = [r for r in rooms if ~(r.value[1] & Directions.RIGHT)]
        return rooms

    def print_map(self):
        if not self.map:
            return

        min_x = min(x for x, _ in self.map)
        max_x = max(x for x, _ in self.map)
        min_y = min(y for _, y in self.map)
        max_y = max(y for _, y in self.map)

        room_height =  5
        room_width = 7

        output = []

        for y in range(max_y, min_y -1, -1):
            row_lines = [""] * room_height

            for x in range(min_x, max_x + 1):
                room = self.map.get((x, y))

                if room is None:
                    lines = [" " * room_width] * room_height
                else:
                    lines = Rooms.tostr(room).splitlines()

                for i, line in enumerate(lines):
                    row_lines[i] += line

            output.extend(row_lines)

        print("\n".join(output))


    # pretty print
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Dungeon<{self.map}>"

__all__ = ["Dungeon"]

# test case
if __name__ == "__main__":
    Dungeon().print_map()
