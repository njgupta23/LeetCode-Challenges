# Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]



def sortColors(nums):

    import random
    
    def _sortColors(nums, first, last):
        if first < last:
            pivot = first + random.randrange(last - first + 1)
            nums[pivot], nums[last] = nums[last], nums[pivot]
            
            pivot = first
        
            for i in range(pivot, last):
                if nums[i] <= nums[last]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            nums[pivot], nums[last] = nums[last], nums[pivot]
                
            _sortColors(nums, first, pivot - 1)
            _sortColors(nums, pivot + 1, last)
    
    _sortColors(nums, 0, len(nums)-1)
