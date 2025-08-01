import asyncio


async def add_numbers(x: int, y: int) -> int:
    return x + y


async def main() -> None:
    result1 = await add_numbers(10 , 20)
    result2 = await add_numbers(2 , 3)
    
    print("result 1 : ", result1)
    print("result 2 : ", result2)
    
    
asyncio.run(main())
    