#!/usr/bin/env python3
"""Function to get a tuple from to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of int and float"""
    return (k, v**2)
