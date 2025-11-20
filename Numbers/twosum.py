"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

import itertools

def twoSum(nums, target):
    # check if there are duplicates in the nums list
    if len(nums) != len(set(nums)):
        raise ValueError("Duplicate values found in input list")
    indices = 2
    # Get combinations of elements of size 2 then find the target sum
    combos = list(itertools.combinations(nums, indices))
    #print(combos)
    for c in combos:
        if sum(c) == target:
            # identify the indices
            return [nums.index(c[0]), nums.index(c[1])]

nums = [3,2,4]
target = 6
ret = twoSum(nums, target)
print(f"Indices of elements in {nums} whose sum is {target}: {ret}")