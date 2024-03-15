#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

    Args:
        multiplier: A float value to be used as a multiplier.

    Returns:
        A function that takes a float argument and returns the result of multiplying that float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
