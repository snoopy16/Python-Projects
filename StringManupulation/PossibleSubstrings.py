"""
Program that prints out all possible substrings in a string
Given a string print out substrings such as abcd => a, ab, abc, abcd, bc, bcd, b, c, d, cd
"""
import itertools

def printSubstrings(string):
    possible_substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            possible_substrings.append(string[i:j])
    return possible_substrings

if __name__=='__main__':
    string = "abc"
    ret = printSubstrings(string)
    print(f"All possible substrings {ret} for string \"{string}\"")
    # Now print the substrings with min and max length
    length_dict = {len(i):i for i in ret}
    my_max = length_dict[max(length_dict.keys())]
    my_min = length_dict[min(length_dict.keys())]
    print(f"Max Length of substring: {my_max}, Min Length of substring: {my_min}")