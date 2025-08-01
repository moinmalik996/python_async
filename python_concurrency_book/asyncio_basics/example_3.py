# Introducing long-running coroutines with sleep

import asyncio

async def hello_message():
    await asyncio.sleep(1)
    return "Hello World"


async def main():
    message = await hello_message()
    print(message)
    

asyncio.run(main())
    