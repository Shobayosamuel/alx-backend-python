#!/usr/bin/env python3
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it 
    into a new function task_wait_n
    """
    vals = []
    for i in range(n):
        vals.append(task_wait_random(max_delay))
    delays = []
    for task in asyncio.as_completed(vals):
        delay = await task
        delays.append(delay)
    return delays
