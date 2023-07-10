#!/usr/bin/env python3
"""Function to wait for random sleeptime"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return the random values"""
    ans = random.random() * max_delay
    await asyncio.sleep(ans)
    return ans
