# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# we will be using two *pointers* (doesnt exist in python) to use as a leading and lagging node as we iterate through the list
# to determine if a linked list connects to itself, we have create two objects and set it to to the head of the list
# if the linked list is empty, then return false
# else: as long as the next 2 nodes after the leading one aren't null, move the leading pointer twice over while the lagging one only once. 
# check after every iteration of the loop if equal, and if so return True


class Solution(object):
    def hasCycle(self, head):
        lead = head
        lag = head

        if head == null:
            return False
        
        while lead.next is not None and lead.next.next is not None:
            lag = lag.next
            lead = lead.next.next
            if lead == lag: # can also do lag.next == lead.next.next, but this is easier to read
                return True
        
        return False