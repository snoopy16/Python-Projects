# Python itertools is a module that provides various functions that work on iterators
# to produce complex iterators. It is used for time efficiency

import operator
import itertools

import time

L1 = [1,2,3]
L2 = [2,3,4]

t1=time.time()
a, b, c = map(operator.mul, L1, L2)
t2 = time.time()
print(a, b, c)

print("time taken by map function")
print("Time: {}".format(t2-t1))

t1 = time.time()
for i in range(len(L1)):
    print(L1[i] * L2[i], end= " ")
t2 = time.time()

print("time taken by for loop")
print("Time: {}".format(t2-t1))

# Infinite iterator
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i)


# Combinators: Product, Permutation
print(list(itertools.product([1,2,3], repeat=3))) # ALL POSSIBLE PERMUTATIONS
print(list(itertools.permutations([1,2,3])))  # EXCLUDES REPEATED ENTRIES
# >>> list(itertools.combinations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 3)]
# >>> list(itertools.permutations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# >>>