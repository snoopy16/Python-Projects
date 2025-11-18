# Ask the user for a string and print out whether this string is a palindrome or not
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# example: aba saas attitta
# used python reversed or string slicing string[::-1]

#s = str(input("Enter a string "))
#reversed_string = s[::-1]
#reversed_string = "".join(reversed(s))
#if (s == reversed_string):
#    print("Its a palindrome ")
#else:
#    print("Its not a palindrome")


# reverse using stack pop
# Stack has first in last out which is similar to reversing a string operation

def createStack():
    myStack = []
    return myStack

def isEmpty(stack):
    if len(stack) == 0:
        return True

def sizeofStack(stack):
    return len(stack)

def pushElements(stack, item):
    stack.append(item)


def popElements(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def main():

    s = str(input("Enter a string "))

    n = len(s)

    # creates an empty stack
    stack = createStack()

    # pushes elements in a stack
    for i in range(0, n):
        pushElements(stack, s[i])

    temp_string = ""
    # pops elements in a stack into a temporary string
    for i in range(0, n):
        temp_string += popElements(stack)

    # Check to see if the string is a palindrome or not
    if s == temp_string:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is NOT a palindrome")

if __name__ == '__main__':
    main()