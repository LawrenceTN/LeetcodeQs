# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# not the optimal way, but enumerate through list and use 'continue' when at blocker number matches the index
# blocker number will count up from 0 to the range of the list
# append the product without the blocker index to a new array  

class Solution(object):
    def productExceptSelf(self, nums):
        blocker = 0
        array = []
        for blocker in range(len(nums)):
            product = 1
            for i, num in enumerate(nums):
                if i == blocker:
                    continue
                product *= num
            array.append(product)