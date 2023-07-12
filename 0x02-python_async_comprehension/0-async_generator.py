#!/usr/bin/env python3
"""Function to generate random numbers"""


import asyncio
import random


async def async_generator():
    """Yield the random integers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
