"""
Print the number as even or odd
Get number from user = type integer. If its a non integer, return error
"""


x = input("Please enter a number (integer only)") # 1 ,2, 0, -2, string x, float x
try:
    if int(x) % 2 == 0:
        print("Even number ")
    else:
        print("Odd number 6")
except ValueError as e:
    print(e)