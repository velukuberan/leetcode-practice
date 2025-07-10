import pytest
from src.calculator import add, subtract, multiply, divide


def test_add() -> None:
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract() -> None:
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_multiply() -> None:
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1


def test_divide() -> None:
    assert divide(1, 2) == 0.5
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1

    # Test divide by zero error
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
