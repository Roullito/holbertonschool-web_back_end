#!/usr/bin/env python3
"""Basic annotations - sum_mixed_list."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of integers and floats and return the result as float"""
    return sum(mxd_lst)
