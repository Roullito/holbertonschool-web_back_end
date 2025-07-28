#!/usr/bin/env python3
"""Concurrent coroutines"""


from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines concurrently and return sorted delays"""
    delays_coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*delays_coroutines)
    return sorted(delays)
