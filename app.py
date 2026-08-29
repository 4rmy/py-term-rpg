from items import Item
from player import Player
from dungeon import Dungeon

class Game():
    active_profile: Player
    active_dungeon: Dungeon or None

    def __init__(self) -> None:
        active_profile = Player()

    def startDungeon(self):
        active_dungeon = Dungeon()

if __name__ == "__main__":
    Game()

# TODO:
# ITEMS
# - Item Rarities
#   - Weighted Loot
# PLAYER
# - Player Stat Calculations
# - Player loading and saving
# DUNGEON
# - Add enemies
#   - enemy superclass
# - Add loot
# TUI (Game controller)
# - Pretty-fy TUI
