def list_sum(arr):
    """
    Recursively calculates the sum of numbers in a list.

    Parameters:
    arr (list): List of numbers to sum.

    Returns:
    int or float: Sum of all numbers in the list.
    """
    if len(arr) == 0:
        return 0
    else:
        return list_sum(arr[:-1]) + arr[-1]

if __name__ == "__main__":
    example_list = [1, 2, 3, 4]
    result = list_sum(example_list)
    print(f"Sum of {example_list} is {result}")