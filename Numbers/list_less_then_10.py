"""
Problem: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Given a list of numbers, print out all the elements less than 5 (one at a time)
example: [4,5,6,7,8,10,0,-4] ==> [4,0,-4]
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# complexity: n
for i in a:
    if i < 5:
        print(i, end=" ")

print("\nExtra 1: ")
# Extra 1: instead of printing elements one by one print out a new list of elements less than 5
less_than_5 = []
for i in a:
    if i < 5:
        less_than_5.append(i)

print(less_than_5)

print ("\n Extra 2: ")
# Extra 2: Write this in one line of python
print([i for i in a if i < 5])

print("\n Extra 3: ")
# Extra 3: Ask a user for a number and return a list that contains only elements from original list a that are smaller
# that are smaller than than number given by the user
x = int(input(f" Give me a number from this list {a}: "))

print([i for i in a if i < x])
