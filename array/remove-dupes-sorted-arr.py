# Remove Duplicates from Sorted Array

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example:
# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.


def removeDuplicates(nums):

    i = len(nums) - 1

    while i > 0:
        if nums[i] == nums[i-1]:
            nums.pop(i)
        i -= 1

    return len(nums)
