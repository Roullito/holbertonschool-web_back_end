#!/usr/bin/env python3
"""Async comprehension with async generator"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension.

    This coroutine function uses async comprehension to collect all values
    from the async_generator function into a list. It will wait for all
    10 random floating-point numbers to be generated.

    Returns:
        List[float]: A list containing 10 random floating-point numbers
                    between 0 and 10.
    """
    return [i async for i in async_generator()]
