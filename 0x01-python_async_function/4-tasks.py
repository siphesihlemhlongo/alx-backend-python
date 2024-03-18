#!/usr/bin/env python3
import asyncio
from asyncio import Task
from random import uniform
from typing import List

# Assuming task_wait_random is defined in the same file as wait_random
from . import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)

# Example usage
async def main():
    n = 5
    max_delay = 10
    delays = await task_wait_n(n, max_delay)
    print("Delays:", delays)

# Run the main coroutine
asyncio.run(main())
