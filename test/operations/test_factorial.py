from operations.Factorial import calculate_factorial


def test_factorial():
    result = calculate_factorial(0)
    assert result == 1
    pass
