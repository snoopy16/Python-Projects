"""
Generate a Fibonacci list of numbers. How many numbers to generated is defined by users
Example https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
n=6, series = 1, 1, 2, 3, 5, 8
"""
try:
    n = int(input("How many numbers in Fibonacci series? Minimum 2 "))
except ValueError as e:
    print(e)
    exit(1)

if n <= 1:
    print("Please enter number higher than 2")
    exit(1)

series = [1, 1]

for i in range(1, n-1):
    try:
        series.append(series[i] + series[i-1])
    except IndexError:
        continue

print(series)

