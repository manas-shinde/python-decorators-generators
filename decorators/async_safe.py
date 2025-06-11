import asyncio
import functools


def async_safe(func):
    """Wrap a sync function to make it awaitable in async contexts."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: func(*args, **kwargs))
    return wrapper
