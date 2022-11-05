from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Flavor(str, Enum):
    chocolate = 'chocolate'
    vanilla = 'vanilla'
    strawberry = 'strawberry'
    mint = 'mint'
    coffee = 'coffee'
    peanut_butter = 'peanut butter'


class Topping(str, Enum):
    sprinkles = 'sprinkles'
    hot_fuge = 'hot_fuge'
    cookies = 'cookies'
    brownie = 'brownie'
    whipped_cream = 'whipped_cream'
    strawberries = 'strawberries'


@dataclass
class IceCreamMix:
    name: str
    flavor: Flavor
    toopings: Tuple[Topping, ...]
    scoops: int
