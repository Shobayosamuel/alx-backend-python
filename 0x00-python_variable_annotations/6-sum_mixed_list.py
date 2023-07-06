#!/usr/bin/env python3
"""Function to get the sum of mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list as a float"""
    return sum(mxd_lst)
