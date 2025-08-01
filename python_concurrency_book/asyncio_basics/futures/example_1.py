# futures introduction

import asyncio
from asyncio import Future

async def main():
    
    future = Future()

    print(f"Is my future done: {future.done()}")

    future.set_result(42)

    print(f"Is my future done: {future.done()}")
    print(f"What is the result of my future: {future.result()}")

    
    
asyncio.run(main())