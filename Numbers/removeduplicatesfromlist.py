"""
Program to remove duplicates from a list and return unique elements
Example: For a given list - [0, 0, 0, 0, 3] return [0, 3]
"""

def removeDuplicates(nums) -> int:
    # identify duplicates
    copy_of_nums = nums.copy()
    for element in copy_of_nums:
        if nums.count(element) > 1:  # There are duplicates
            nums.remove(element)
            nums.append("_")
    unique_elements = len(nums) - nums.count("_")
    return nums[0:unique_elements]

if __name__ == '__main__':
    l = [0,0,0,0,3]
    print(l)
    nums = removeDuplicates(l)
    print(nums)