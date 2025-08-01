import asyncio
from .profiling_coroutine import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} seconds.")
    await asyncio.sleep(delay_seconds)
    print(f"Finished sleeping for {delay_seconds} seconds.")
    return delay_seconds