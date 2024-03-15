#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing elements of the input list along with their lengths.

    Args:
        lst: A list of strings.

    Returns:
        A list of tuples where each tuple contains an element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
