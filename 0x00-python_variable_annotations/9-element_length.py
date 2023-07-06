#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence
"""Function to get a tuple from a string"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a tuple generated from the list argument"""
    return [(i, len(i)) for i in lst]
