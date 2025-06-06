import pytest
from decorators.validate_types import validate_types


@validate_types
def add(x: int, y: int) -> int:
    return x + y


def test_validate_types_success():
    assert add(2, 3) == 5


def test_validate_types_arg_error():
    with pytest.raises(TypeError):
        add("2", 3)


def test_validate_types_return_error():
    @validate_types
    def broken_add(x: int, y: int) -> str:
        return x + y  # Will return int, violates str

    with pytest.raises(TypeError):
        broken_add(1, 2)
