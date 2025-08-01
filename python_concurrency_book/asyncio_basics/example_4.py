import asyncio
from utils import delay


async def add_numbers(x: int, y: int) -> int:
    return x + y


async def hello_message():
    await asyncio.sleep(1)
    return "Hello World"


async def main():
    message = await hello_message()
    result = await add_numbers(10, 29)
    await delay(1)
    print(message)
    print(result)
    
    
asyncio.run(main())
    