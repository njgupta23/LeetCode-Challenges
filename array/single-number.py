# Single Number

# Given a non-empty array of integers, 
# every element appears twice except for one. 
# Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?


def singleNumber(self, nums):
    
    for n in range(0, len(nums), 2):
        if n == len(nums)-1:
            return nums[n]
        if nums[n] != nums[n+1]:
            return nums[n]
