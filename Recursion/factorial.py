def factorial(f):
    """
    Calculate the factorial of a non-negative integer f using recursion.

    Parameters:
    f (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of f (f!)

    Raises:
    ValueError: If f is negative.
    """
    if f < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)

if __name__ == "__main__":
    number = 4
    result = factorial(number)
    print(f"{number}! = {result}")
