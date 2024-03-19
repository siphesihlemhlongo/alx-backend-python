#!/usr/bin/env python3
import asyncio
import random
from typing import List

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Parameters:
        max_delay (int): The maximum delay in seconds (default is 10).
    
    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.
    
    Parameters:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.
    
    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

# Test the wait_n coroutine
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
