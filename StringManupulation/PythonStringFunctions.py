# Here is a list of useful "built-in" string functions in python
# source: https://www.w3schools.com/python/python_ref_string.asp

# 1. string.count(): Returns the number of times a sepcified value occurs in a string
s = "this S SOMETHING Great going ON"
print(s.count("s"))  # This is case-sensitive

# 2. string.find(): Searches the string for a specified value and returns the position of where it was found
print(s.find("s")) # first occurance of letter s
print(s.find("q")) # return -1
#print(s.index("q")) # raise ValueError: substring not found

# 3. string.format(): Insert specified values or strings in placeholders
print("My name is {}, my age is {}".format("John", 89))

# 4. string.isalnum(): Checks if all the characters in the text are alpha numeric
j="compnay12"
print(j.isalnum())
j="_+"
print(j.isalnum())

# 5. string.isalpha(): Returns true is all the characters are alphabets a-zA-Z, no numbers, no special chars
# 6. string.isdigit(), string.isnumeric()

# 7. s.lstrip() s.rstrip(): Remove spaces from right or left
s = "    banana   "
print(s.lstrip().rstrip())
txt = ",,,,,rrttgg.....banana....rrr"
print( txt.strip(",rtg."))

# 8. s.splitlines(): Splits a string with \n into array elements
s="Today is Monday \n Its a great day so far \n And the weather is warm and sunny "
print(s.splitlines())

# 9. Encoding
data="hello"
print(data.encode("utf-8"))
print(data.encode(encoding="ascii"))