"""
Program to identify if a number if palindrome or not
For example: 12321 is a Palindrome but 1231 is not a palindrome
"""

def isPalindrome(x: int) -> bool:
    palindrome = False
    s = str(x)
    if s == "".join(list(reversed(s))):
        palindrome = True
    return palindrome

if __name__ == '__main__':
    try:
        x = int(input("Enter a number: "))
        print("Is Palindrome: ", isPalindrome(x))
    except ValueError as e:
        print(e)