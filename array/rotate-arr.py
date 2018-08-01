# Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]

# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums, k):
        
    if len(nums) == 1:
        return
    
    for i in range(k):
        save = nums[0]
        nums[0] = nums[-1]
        
        for j in range(len(nums)-1, 1, -1):
            nums[j] = nums[j-1]
            
        nums[1] = save
