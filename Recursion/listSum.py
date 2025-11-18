# Pring out sum of numbers in a list using Recursion
# listSum([array])
# array = [1, 2, 3, 4], listSum = 1+2+3+4 = 10

def listSum(arr):
    arr_size = len(arr)
    if arr_size == 0:
        return 0
    else:
        return listSum(arr[:arr_size - 1]) + arr[arr_size -1]


print(listSum([1,2,3,4]))