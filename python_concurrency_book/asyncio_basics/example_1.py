import asyncio


async def add_numbers_coroutine(x) -> int:
    return x + 1


def add_numbers(x) -> int:
    return x + 1


print(add_numbers(1))
# print(add_numbers_coroutine(1)) # it will throw never awaited error


result = asyncio.run(add_numbers_coroutine(1))

print(result)