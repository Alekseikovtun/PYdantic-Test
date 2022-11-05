from pydantic import BaseModel, Field, validator, root_validator
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
    hot_fudge = 'hot_fuge'
    cookies = 'cookies'
    brownie = 'brownie'
    whipped_cream = 'whipped_cream'
    strawberries = 'strawberries'


class Container(str, Enum):
    cup = 'cup'
    cone = 'cone'
    waffle_cone = 'waffle_cone'


class IceCreamMix(BaseModel):
    name: str
    container: Container
    flavor: Flavor
    toppings: Tuple[Topping, ...]
    scoops: int = Field(..., gt=0, lt=5)

    @validator('toppings')
    def check_toppings(cls, toppings):
        if len(toppings) > 4:
            raise ValueError('Too many toppings')
        return toppings

    @root_validator
    def check_cone_toppings(cls, values):
        container = values.get('container')
        toppings = values.get('toppings')
        if container == Container.cone or container == Container.waffle_cone:
            if Topping.hot_fudge in toppings:
                raise ValueError('Cones cannot have hot fudge')
        return values
