#!/usr/bin/env python3
"""Measure runtime of async comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension 4 times
    in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
