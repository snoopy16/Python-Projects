# Write a function that takes a list of words as input, and returns
# a list of those words bucketized by anagrams.
#
# "Anagram" definition: a word, phrase, or name formed by rearranging
# the letters of another, such as cinema, formed from iceman.
#
# Example:
#
# anagram_buckets(word_list)
#
# Input:  ["star", "rats", "car", "arc", "arts", "stars"]
# Output:  [ ["star", "rats", "arts"], ["car", "arc"], ["stars"] ]

# Assumption: all lower case, alphabetical. No ordering is not required alphabatical order.

def anagram_buckets(word_list):
    # loop through word_list and find sorted for each
    # group sorted items together in a sub-list
    # return actual list
    # {"arst": ["star", "rats", "arts"], "acr": ["car", "arc"]}
    dictionary_anagrams = {}
    for word in word_list:
        key = "".join(sorted(word))
        if key in dictionary_anagrams.keys():
            dictionary_anagrams[key].append(word)
        else:
            dictionary_anagrams[key] = [word]

    return dictionary_anagrams.values()

word_list = ["star", "rats", "car", "arc", "arts", "stars"]
print(anagram_buckets(word_list))
