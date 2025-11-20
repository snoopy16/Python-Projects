def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position in the Fibonacci sequence (0-based index).

    Returns:
    int: The Fibonacci number at position n.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

if __name__ == "__main__":
    try:
        nterms = int(input("What is the length of the Fibonacci series? "))
        if nterms <= 0:
            print("Please enter a positive number > 0.")
            exit(0)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(0)

    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacci(i))
