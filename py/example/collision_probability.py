#!/bin/env python3
import sys
import functools
sys.setrecursionlimit(10000)


@functools.cache
def probability(total: int, n: int) -> float:
    if n <= 0:
        return 1
    return probability(total, n - 1) * (1 - n / total)
