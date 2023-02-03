# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        curr = head
        nums = []

        while curr is not None:
            nums.append(curr.val)
            curr = curr.next

        rev = nums[::-1]

        if (nums == rev):
            return True
        else:
            return False