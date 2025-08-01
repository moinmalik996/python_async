# Running multiple tasks concurrently


import asyncio
from utils import delay


async def main():
    
    delay_1 = asyncio.create_task(delay(3))
    delay_2 = asyncio.create_task(delay(3))
    delay_3 = asyncio.create_task(delay(3))
    
    await delay_1
    await delay_2
    await delay_3
    


asyncio.run(main())
    
