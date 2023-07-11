#!/usr/bin/env python3
"""Function to wait n number of times"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times"""
    ans = []
    for i in range(n):
        ans.append(wait_random(max_delay))
    delays = []
    for tsk in asyncio.as_completed(ans):
        delay = await tsk
        delays.append(delay)
    return delays
