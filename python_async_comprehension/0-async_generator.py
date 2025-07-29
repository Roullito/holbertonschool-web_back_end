#!/usr/bin/env python3
"""Async generator that yields random numbers"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields 10 random floats between 0-10 with 1s delay between each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
