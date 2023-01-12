# Given an integer array nums, find the subarray which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# unsure on how fool-proof this is, but knowing that the first number would be an answer if subsequent values are less than it
# we assign that value to maxSub.
# next, iterate through the list, adding each number to the curSum. if we ever find curSum to have less than 0, we reser to 0
# each iteration, we check what is larger between maxSub and curSum. whatever it is, assign it to maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = nums[0]
curSum = 0

for num in nums:
    if curSum < 0:
        curSum = 0
    curSum += num
    maxSub = max(maxSub, curSum)
print(maxSub)

