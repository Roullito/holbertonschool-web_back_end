#!/usr/bin/env python3
"""Async generator that yields random numbers"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields 10 random floating-point numbers.

    This coroutine function generates random numbers between 0 and 10,
    with a 1-second delay between each yield operation.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
