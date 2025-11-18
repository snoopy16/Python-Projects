# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

valid_dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}

def isValid(s: str) -> bool:
    # Even number of chars in parenthesis, square brackets and curly braces
    # create a map of allowed pairs
    # we find a pair in s, replace with empty space until we are left with string of length 0
    for i in s:
        if i in valid_dict.keys(): #we've opening parenthesis
            try:
                open = s.index(i)  # Index of opening parenthesis
                close = s.index(valid_dict[i])  # Index of closing parenthesis

                diff = close - open  # difference should be even number 1, 3, 5
                if diff % 2 == 0:
                    break

                s = s.replace(i, "")
                s = s.replace(valid_dict[i], "")
            except ValueError:
                break


    print(s)
    if len(s) == 0:
        return "true"
    else:
        return "false"


s = input("Please provide a string with parenthesis, brackets, etc: ")
print(isValid(s))
