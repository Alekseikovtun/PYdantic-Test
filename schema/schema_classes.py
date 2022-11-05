from pydantic import BaseModel, Field, validator
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
    toppings: Tuple[Topping, ...]
    scoops: int = Field(..., gt=0, lt=5)

    @validator('toppings')
    def check_toppings(cls, toppings):
        if len(toppings) > 4:
            raise ValueError('Too many toppings')
        return toppings
