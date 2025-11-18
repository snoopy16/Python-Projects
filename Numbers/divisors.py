"""
Practice Assignment: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
Ask user for a number, print out list of divisors for that number.
For example: 26; divisors: 1, 2, 13, 26
Algorithm: value % divisor == 0
Integer, Float? 0 and 0.0 as remainders
""" 

try:
    x = int(input("Please enter a number: "))  # TODO:  we are passing integer
    # check the remainder
    # Time complexity: n
    for i in range(1, x+1):
        if x % i == 0:
            print(i, end=" ")

except ValueError as e:
    print("Please enter a positive integer: %s", e)