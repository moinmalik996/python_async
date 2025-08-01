"""
CPU bound task along side a long running I/O bound task.
"""

import asyncio
from utils import delay, async_timed


@async_timed()
async def cpu_bound_task():
    counter = 0
    for i in range(1, 100000000):
        counter += 1
    return counter

@async_timed()
async def main():
    
    task_one = asyncio.create_task(cpu_bound_task())
    task_two = asyncio.create_task(cpu_bound_task())
    task_three = asyncio.create_task(delay(3))
    
    
    await task_one
    await task_two
    await task_three

if __name__ == "__main__":
    asyncio.run(main())