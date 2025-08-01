"""
This decorator function will allow us to profile 
the timing of the coroutine.
"""

import functools
import time
from typing import Callable, Any


def async_timed():
    
    def wrapper(func: Callable) -> Callable:
        
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            
            print(f"Starting {func} with {args} and {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Finished {func} in {total:.3f} second(s)")
            
        return wrapped
    
    return wrapper
        
            