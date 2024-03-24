#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v as arguments and returns a tuple.

    The first element of the tuple is the string k.
    The second element is the square of the int/float v and is annotated as a float.

    Args:
        k: A string.
        v: An integer or a float.

    Returns:
        A tuple containing the string k and the square of the int/float v.
    """
    return (k, float(v) ** 2)
