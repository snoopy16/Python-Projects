"""
Python Program to find all anagrams in a list of strings.
An anagram string is a word or phrase formed by rearranging the letters of another, 
using all original letters exactly once. For two strings to be anagrams,
they must contain the same characters with the same frequency, but in a different order
"""
from collections import Counter

my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

# Uses lambda expression that defines an anonymous function that 
# can take any number of arguments but evaluates and returns only one expression. 
# Counter is used to count the occurrences of elements within an iterable (like a list, string, or tuple)
is_anagram = lambda x: Counter(x) == Counter(str)

# The filter() function in Python is used to construct an iterator from elements =
# of an iterable for which a function returns true. 
# It provides a concise way to select specific items from a sequence based on a condition.
print(list(filter(is_anagram, my_list)))