#!/usr/bin/env python3
import asyncio
from asyncio import Task
from random import uniform
from typing import Callable

# Assuming wait_random is defined in 0-basic_async_syntax.py
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> Task:
    async def _task_wait_random():
        return await wait_random(max_delay)

    return asyncio.create_task(_task_wait_random())

# Example usage
async def main():
    max_delay = 5
    task = task_wait_random(max_delay)
    result = await task
    print("Result:", result)

# Run the main coroutine
asyncio.run(main())
