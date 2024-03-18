#!/isr/bin/env python3
import asyncio
from random import uniform
from typing import List

async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)

async def main():
    # Example usage
    n = 5
    max_delay = 10
    delays = await wait_n(n, max_delay)
    print("Delays:", delays)

# Run the main coroutine
asyncio.run(main())
