#!/usr/bin/env python3
"""Function to wait for random sleeptime"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """Return the random values"""
    ans = random.randint(0, max_delay)
    asyncio.sleep(ans)
    return ans
