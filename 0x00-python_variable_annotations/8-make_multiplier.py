#!/usr/bin/env python3
"""Function that retuns a fuction"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that returns a float"""
    def multiply(val: float) -> float:
        return multiplier * val
    return multiply
