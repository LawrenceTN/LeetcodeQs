# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# go through the array of numbers, adding the number as a key and it's index as the value.
# before we do this however, check if the target minus the current number we're at, exists already in the dict
# if so, then return the value of the difference and the current numbers index.


nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    myDict = {}
    for i, num in enumerate(nums):
        if target-num in myDict:
            return i, myDict[target-num]
        myDict[num] = i
