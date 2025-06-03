import pytest
from decorators.retry_decorator import retry_on_exception

counter = {"calls": 0}


@retry_on_exception(retries=3, delay=0)
def flaky_function():
    counter["calls"] += 1
    if counter["calls"] < 3:
        raise ValueError("Fail")
    return "success"


def test_retry_on_exception():
    counter["calls"] = 0
    result = flaky_function()
    assert result == "success"
    assert counter["calls"] == 3
