# Example: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# Write one line of python tht takes the list a and makes a new list that only has even numbers

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Print Even numbers in a list")
print([i for i in a if i%2 == 0])