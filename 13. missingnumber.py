# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array. 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

# noticing the elemeents of the list, it always starts from 0 to whatever the length is specific of the list
# therefore, the elements in the list must be comprised of 0 to n-1
# using an XOR with the length of the list with the contents and index of the list, it'll find the missing number automatically 

class Solution(object):
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing = missing^num
            missing = missing^i
        return missing