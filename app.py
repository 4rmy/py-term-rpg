from items import Item
from player import Player
from dungeon import Dungeon

class Game():
    active_profile: Player
    active_dungeon: Dungeon


if __name__ == "__main__":
    print(Dungeon())
    Game()

# TODO:

# ITEMS
# - Item Rarities
#   - Weighted Loot

# PLAYER
# - Player Stat Calculations
# - Player loading and saving

# DUNGEON
# - Dungeon wave function collapse

# TUI (Game controller)
# Pritty-fy TUI
