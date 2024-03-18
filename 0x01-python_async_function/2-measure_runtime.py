#!/usr/bin/env python3
import asyncio
from typing import List
from time import time

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

def measure_time(n: int, max_delay: int) -> float:
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n

# Test the measure_time function
n = 5
max_delay = 9
print(measure_time(n, max_delay))
