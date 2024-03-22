#!/usr/bin/env python3
from typing import List
from random import randint

async def async_comprehension() -> List[float]:
    async_gen = async_generator()
    random_numbers = [await num async for num in async_gen]
    return random_numbers
