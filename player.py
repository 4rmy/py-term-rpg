from items import Item

class Player():
    coins: int = 0
    
    max_health: int = 20
    health: int = 20
    
    strength: int = 20
    intelegence: int = 20
    stamina: int = 20

    inventory: list[Item] = []

    # TODO: save to file (compressed)
    # TODO: load from file

__all__ = ["Player"]

