# The basics of creating tasks

import asyncio
from utils import delay

async def add_one(x: int) -> int:
    return x + 1

async def message():
    await delay(1)
    return "Hello World"

async def main():
    msg = await message()
    result = await add_one(1)
    print(result)
    print(msg)
    
    
asyncio.run(main())