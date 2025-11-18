"""
Program to remove duplicates from a list
"""

def removeDuplicates(nums) -> int:
    # identify duplicates
    copy_of_nums = nums.copy()
    for element in copy_of_nums:
        if nums.count(element) > 1:  # There are duplicates
            nums.remove(element)
            nums.append("_")

    unique_elements = len(nums) - nums.count("_")
    return unique_elements, nums

l = [0,0,0,0,3]
print(l)
ret, nums = removeDuplicates(l)
print(ret, nums[0:ret])