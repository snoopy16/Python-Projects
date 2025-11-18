"""
Ask the user for a string and print out whether this string is a palindrome or not
ttps://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
example: aba saas attitta
This example is creted Using anonymous function Lambda and filter
"""
my_list = ["geeks", "geeg", "keek", "practice", "aa"]

filtered_list = list(filter(lambda x: x == "".join(list(reversed(x))), my_list))

print(my_list, filtered_list)
