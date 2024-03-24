#!/usr/bin/env python3
import asyncio
from random import uniform

def wait_random(max_delay=10):
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))

# Test the task_wait_random function
async def test(max_delay: int) -> None:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
