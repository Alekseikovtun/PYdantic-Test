from schema.schema_classes import (
    IceCreamMix, Flavor, Topping
)


def main():
    ice_cream_mix = IceCreamMix(
        'SuPPer',
        Flavor.peanut_butter,
        (Topping.brownie, Topping.sprinkles),
        2
    )
    return ice_cream_mix
