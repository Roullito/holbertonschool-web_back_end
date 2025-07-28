#!/usr/bin/env python3
"""
Basic async syntax module.

This module contains a simple asynchronous function that demonstrates
basic async/await syntax with random delays.
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds (default: 10)

    Returns:
        float: The actual delay time that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
