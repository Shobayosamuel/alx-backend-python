#!/usr/bin/env python3
"""Function to safely get the value"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Return the value of the key given"""
    if key in dct:
        return dct[key]
    else:
        return default
