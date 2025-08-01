# task cancellation

import asyncio
from asyncio import CancelledError
from utils import delay


async def main():
    
    long_task = asyncio.create_task(delay(10))
    
    seconds_consumed = 0
    
    while not long_task.done():
        await asyncio.sleep(1)
        seconds_consumed = seconds_consumed + 1
        if seconds_consumed == 5:
            long_task.cancel()        
        else:
            print("Task not completed, Checking in a minute")
            
    try:
        await long_task
    except CancelledError:
        print("Our Task has been cancelled")
        

asyncio.run(main())