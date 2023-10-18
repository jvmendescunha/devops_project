
def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial

# Example usage
number = 4
result = calculate_factorial(number)
print(f'The factorial of {number} is: {result}')
