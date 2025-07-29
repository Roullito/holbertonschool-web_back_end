#!/usr/bin/env python3
"""Async comprehension with async generator"""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using async comprehension.

    This coroutine function uses async comprehension to collect all values
    from the async_generator function into a list. It will wait for all
    10 random floating-point numbers to be generated.
    """
    return [i async for i in async_generator()]
