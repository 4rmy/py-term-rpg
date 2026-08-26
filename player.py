from items import Item

class Player():
    coins: int
    
    max_health: int
    health: int
    
    strength: int
    intelegence: int
    constitution: int

    inventory: list[Item]

__all__ = ["Player"]
