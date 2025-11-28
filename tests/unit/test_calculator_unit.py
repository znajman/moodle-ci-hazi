# tests/unit/test_calculator_unit.py

from calculator import Calculator

def test_add_two_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract_two_numbers():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_divide_two_numbers():
    calc = Calculator()
    assert calc.divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    calc = Calculator()
    try:
        calc.divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        assert True
