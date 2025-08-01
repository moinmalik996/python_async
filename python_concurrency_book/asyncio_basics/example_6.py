# The basics of creating tasks

import asyncio
from utils import delay


async def main():
    sleep_for_3 = asyncio.create_task(delay(3))
    print("Task Running")
    print(type(sleep_for_3))
    result = await sleep_for_3
    return result


asyncio.run(main())