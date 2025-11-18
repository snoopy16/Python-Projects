"""
Program that prints out all possible substrings in a string
Given a string print out substrings such as abcd => a, ab, abc, abcd, bc, bcd, b, c, d, cd
using lambda + itertools.groupby() + split()
test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3', 'pro_3']
output = [['geek_1', 'geek_4'], ['coder_2', 'coder_3'], ['pro_3']]
"""
from itertools import groupby

# initializing list
test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3', 'pro_3']

# replace with alphabatically sorted list 
test_list = sorted(test_list)

# create an anonymous function baseString to split out string from numbers
baseString = lambda x: x.split("_")[0]

items = {}
for k, g in groupby(test_list, baseString):
    print(k, list(g))