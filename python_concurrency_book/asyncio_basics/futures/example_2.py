# implementing a future object asynchronously

import asyncio
from asyncio import Future


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future
    

async def set_future_value(future: Future) -> None:
    await asyncio.sleep(10)
    future.set_result(100)
    
async def main():
    future = make_request()
    print(f"Is the future is Done : {future.done()}")
    value = await future
    print(f"Is the future is Done : {future.done()}")
    print(f"The Value is = {value}")


asyncio.run(main())