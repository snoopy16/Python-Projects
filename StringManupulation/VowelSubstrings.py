# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

from StringManupulation.PossibleSubstrings import printSubstrings
from collections import Counter

vowels = ["a", "e", "i", "o", "u"]
def vowel_substrings(string):
    vowel_substrings = []
    for i in range(len(string)):
        if string[i] in vowels:
            # We've found the starting letter now print the substrings of all possible length
            for j in range(i, len(string)+1):
                if string[i:j]:
                    vowel_substrings.append(string[i:j])
            
    return vowel_substrings

if __name__=='__main__':
    string = "banana"
    val = {}
    vowel_sub = vowel_substrings(string)
    counter_vowel = Counter(vowel_sub)
    total_substrings = printSubstrings(string)
    counter_total_sub = Counter(total_substrings)
    consonent_sub = counter_total_sub - counter_vowel

    print(f"Total Substrings: {total_substrings}")
    print(f"Vowel Substrings: {vowel_sub}")
    print(f"Consonent Substrings: {list(consonent_sub)}")
   
