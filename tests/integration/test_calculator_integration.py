# tests/integration/test_calculator_integration.py

from calculator import Calculator

def test_complex_calculation_flow():
    """
    This is an 'integration' style test: it uses multiple methods in sequence
    to simulate a slightly more realistic workflow.
    """
    calc = Calculator()

    # Start from 0, add, subtract, divide -> check final result
    result = 0
    result = calc.add(result, 10)      # 10
    result = calc.subtract(result, 3)  # 7
    result = calc.add(result, 5)       # 12
    result = calc.divide(result, 3)    # 4

    assert result == 4
