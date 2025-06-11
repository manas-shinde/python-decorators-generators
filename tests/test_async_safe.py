import asyncio

import pytest
from decorators.async_safe import async_safe


@async_safe
def sync_add(x, y):
    return x + y


@pytest.mark.asyncio
async def test_async_safe():
    result = await sync_add(2, 3)
    assert result == 5
