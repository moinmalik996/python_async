# setting a timeout for coroutine / tasks

import asyncio
from utils import delay


async def main():
    
    long_task = asyncio.create_task(delay(5))
    
    try:
        await asyncio.wait_for(long_task, timeout=3)
        # print(result)
    except asyncio.exceptions.TimeoutError:
        print("We got timeout")
        print(f"Is task cancelled :  {long_task.cancelled()}")
        
        
asyncio.run(main())