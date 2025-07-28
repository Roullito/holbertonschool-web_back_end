#!/usr/bin/env python3
"""Basic annotations - to_kv."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string `k` and the square of `v` as a float.

    Args:
        k (str): The key.
        v (Union[float, int]): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple with the key and the squared value as float.
    """
    return (k, float(v * v))
