#!/usr/bin/env python3
import asyncio
from typing import List
from time import time
from .1-concurrent_coroutines import wait_n  # Importing wait_n from previous file

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay), and returns total_time / n.
    
    Parameters:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.
    
    Returns:
        float: The average time taken for each wait_random call.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n

# Test the measure_time function
n = 5
max_delay = 9
print(measure_time(n, max_delay))
