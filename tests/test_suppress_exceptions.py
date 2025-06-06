from decorators.suppress_exceptions import suppress_exceptions


@suppress_exceptions(default="fallback", exceptions=(ZeroDivisionError,))
def risky_div(x):
    return 10 / x


def test_suppress_success():
    assert risky_div(2) == 5


def test_suppress_zero_division():
    assert risky_div(0) == "fallback"
