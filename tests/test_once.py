from decorators.once import once

call_counter = {"count": 0}


@once
def run_once():
    call_counter["count"] += 1
    return "executed"


def test_once():
    assert run_once() == "executed"
    assert run_once() == "executed"
    assert call_counter["count"] == 1  # should only execute once
