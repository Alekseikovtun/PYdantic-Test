from schema.schema_classes import (
    IceCreamMix, Flavor, Topping
)
from pydantic import ValidationError


def main():
    try:
        ice_cream_mix = IceCreamMix(
            name='idk',
            container='cone',
            flavor=Flavor.chocolate,
            toppings=(Topping.brownie, Topping.cookies),
            scoops=2
        )
        return ice_cream_mix
    except ValidationError as e:
        return e
