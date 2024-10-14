#!/usr/bin/env python3
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with a maximum delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of delays (float) in ascending order.
    """
    # Create a list of awaitable wait_random coroutines
    delays = [await wait_random(max_delay) for _ in range(n)]
    
    # Manually insert the results into the list in ascending order
    return sorted(delays)
