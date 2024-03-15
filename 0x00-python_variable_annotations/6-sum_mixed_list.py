#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst: A list containing integers and floats.

    Returns:
        The sum of the integers and floats in the input list as a float.
    """
    return sum(mxd_lst)
