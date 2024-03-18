#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    # Example usage
    random_delay = await wait_random()
    print(f"Waited for {random_delay:.2f} seconds")

# Run the main coroutine
asyncio.run(main())
