#!/usr/bin/env python3
import asyncio
import time
from typing import List
from wait_random_file import wait_n  # Assuming wait_n is defined in wait_random_file.py

async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

async def main():
    n = 5
    max_delay = 10
    average_time_per_wait = await measure_time(n, max_delay)
    print(f"Average time per wait: {average_time_per_wait:.4f} seconds")

# Run the main coroutine
asyncio.run(main())
