#!/usr/bin/env python3
import asyncio
from typing import List
from random import uniform

async def wait_random(max_delay=10):
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays

# Test the task_wait_n function
n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
