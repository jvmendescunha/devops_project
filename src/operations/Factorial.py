
def calculate_factorial(number: int) -> int:
    """
    Calculates factorial for a number

    :param int number: the input number
    :return int: the factorial of the number
    """
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial
