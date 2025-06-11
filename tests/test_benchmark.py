import time
from decorators.benchmark import benchmark


@benchmark(threshold=0.1)
def slow_func():
    time.sleep(0.1)
    return "done"


def test_benchmark_logs(capsys):
    result = slow_func()
    assert result == "done"
