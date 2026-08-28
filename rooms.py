from enum import IntEnum, Enum, auto
from pprint import pprint

class Directions(IntEnum):
    UP      = 0b1000
    DOWN    = 0b0100
    LEFT    = 0b0010
    RIGHT   = 0b0001
    ALL     = 0b1111
    HORIZ   = 0b0011
    VERT    = 0b1100

class Rooms(Enum):
    START       = (auto(), Directions.UP)
    UP_CAP      = (auto(), Directions.DOWN)
    DOWN_CAP    = (auto(), Directions.UP)
    LEFT_CAP    = (auto(), Directions.RIGHT)
    RIGHT_CAP   = (auto(), Directions.LEFT)
    HORIZ_HALL  = (auto(), Directions.HORIZ)
    VERT_HALL   = (auto(), Directions.VERT)
    INTERSECT   = (auto(), Directions.ALL)
    DL_TURN     = (auto(), Directions.LEFT | Directions.DOWN)
    UL_TURN     = (auto(), Directions.LEFT | Directions.UP)
    DR_TURN     = (auto(), Directions.RIGHT | Directions.DOWN)
    UR_TURN     = (auto(), Directions.RIGHT | Directions.UP)
    L_TEE       = (auto(), Directions.LEFT | Directions.UP | Directions.DOWN)
    R_TEE       = (auto(), Directions.RIGHT | Directions.UP | Directions.DOWN)
    U_TEE       = (auto(), Directions.LEFT | Directions.UP | Directions.RIGHT)
    D_TEE       = (auto(), Directions.RIGHT | Directions.LEFT | Directions.DOWN)
    
    
    @staticmethod
    def ALL():
        return [r for r in Rooms if r != Rooms.START]

    @staticmethod
    def tostr(room):
        return f"+={'   ' if room.value[1] & Directions.UP else '==='}=+\n" + \
                f"|     |\n" + \
                f"{' ' if room.value[1] & Directions.LEFT else '|'} {' ' * (2-len(str(room.value[0]))) + str(room.value[0])}  {' ' if room.value[1] & Directions.RIGHT else '|'}\n" + \
                f"|     |\n" + \
                f"+={'   ' if room.value[1] & Directions.DOWN else '==='}=+"

__ALL__ = ["Directions", "Rooms"]

# test case
if __name__ == "__main__":
    for r in Rooms:
        print(Rooms.tostr(r))
