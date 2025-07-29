#!/usr/bin/env python3
"""Concurrent coroutines"""


from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines concurrently and return sorted delays"""
    delays_coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*delays_coroutines)
    return sorted(delays)
