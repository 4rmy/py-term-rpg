from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Upgrades():
    max_total: int

    strength: int = 0
    intel: int = 0

class Rarity(Enum):
    Common      = auto()
    Uncommon    = auto()
    Rare        = auto()
    Epic        = auto()
    Legendary   = auto()
    Ultimate    = auto()
    Divine      = auto()

class ItemType(Enum):
    Headware    = auto()
    Armor       = auto()
    Weapon      = auto()

@dataclass
class Item():
    item_type: ItemType
    
    name: str

    base_value: int
    
    base_strength: int
    base_int: int

    rarity: Rarity
    upgrades: Upgrades


BORDER_COLOR    = "\x1b[38;5;240m"
RESET           = "\x1b[0m"
def item_color(rarity: Rarity):
    return {
            Rarity.Common: "\x1b[38;5;7m",
            Rarity.Uncommon: "\x1b[38;5;35m",
            Rarity.Rare: "\x1b[38;5;17m",
            Rarity.Epic: "\x1b[38;5;54m",
            Rarity.Legendary: "\x1b[38;5;178m",
            Rarity.Ultimate: "\x1b[38;5;88m",
            Rarity.Divine: "\x1b[38;5;12m"
    }[rarity]

@dataclass
class Weapon(Item):
    def __repr__(self) -> str:
        lines = [
                f"\x1b[38;5;1mPhysical Damage: {self.base_strength + 5 * self.upgrades.strength}",
                f"\x1b[38;5;2mSpell Damage: {self.base_int + 5 * self.upgrades.intel}",
                f"\x1b[38;5;3mValue: {self.base_value * self.rarity.value}",
                self.name
            ]
        length = max(len(o) for o in lines)
        lines.pop()

        return  f"{BORDER_COLOR}.{'='*(length+2)}.\n" + \
                f"|{item_color(self.rarity) + self.name.center(length+2) + BORDER_COLOR}|\n" + \
                f"+{'='*(length+2)}+\n" + \
                f"|{' '*(length+2)}|\n" + \
                ''.join([f"| {RESET}{l.ljust(length+9)}{BORDER_COLOR} |\n" for l in lines]) + \
                f"|{' '*(length+2)}|\n" + \
                f"'{'='*(length+2)}'{RESET}"

@dataclass
class Armor(Item):
    base_health: int

if __name__ == "__main__":
    for r in Rarity:
        Iron_Sword = Weapon(
            ItemType.Weapon,
            "Iron Sword",
            10,
            10,
            2,
            r,
            Upgrades(10)
        )
        print(Iron_Sword)
