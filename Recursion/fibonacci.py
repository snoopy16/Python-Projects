# Print 1, 1, 2, 3, 5, 8, 13

# Function for returning Fibonnacci numbers using recursion
def fibonacci(x):
    # where x is the length of fibonacci series
    if x <= 1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)


nterms = int(input("What is the length of fibonacci series? "))
if nterms <= 0:
    print ("Please enter a positive number >0 ")
    exit(0)

for i in range(nterms):
    print(fibonacci(i))