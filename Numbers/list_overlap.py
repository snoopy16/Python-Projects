"""
Problem: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
two lists - a, b; Return a list that contains elements that are common in both (without duplicates)
listsize? different
Example: a=[1,2,3,4,5,1] b=[1,4,5,6,7] return_list=[1,4,5]
"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Eliminating the duplicates
a = list(set(a))
b = list(set(b))

common_elements = []
for i in a:
    if i in b:
        common_elements.append(i)

print(f"a: {a}\nb: {b}. \nCommon elements between 2 lists: {common_elements}")

# Pythonic way of doing this
# create a function that returns common items in two lists
def commonList(a, b):
    return [i for i in a if i in b]

# Extra 1: Randomly generate two lists to test this
print("\nExtra 1 ")
# Questions: Length of list 1? length of list 2? between 0-100?

length_of_a = 10
length_of_b = 20
a = [random.randrange(0, 100) for i in range(0, length_of_a)]
b = [random.randrange(0, 100) for i in range(0, length_of_b)]

print(f"a: {a}, \nb: {b}")

my_list = commonList(a, b)
print(my_list)