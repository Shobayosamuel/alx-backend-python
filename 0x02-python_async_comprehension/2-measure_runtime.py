#!/usr/bin/env python3
"""Funtion to measure time"""


import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
        Return the time taken to run the list of async comprehension
    """
    start_time = time.time()
    tasks = [async_comprehension(), async_comprehension(),
             async_comprehension(), async_comprehension()]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
