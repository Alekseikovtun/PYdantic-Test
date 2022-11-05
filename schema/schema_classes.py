from pydantic import BaseModel, Field
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


class IceCreamMix(BaseModel):
    name: str
    flavor: Flavor
    toopings: Tuple[Topping, ...]
    scoops: int = Field(..., gt=0, lt=5)
