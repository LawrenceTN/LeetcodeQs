# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# to solve, use two pointers (lead/lag) to find the nth node from the end to delete
# using the lagging node, use it's next linked node to skip the n'th node, basically deleting it from the LL

# [1, 2, 3, 4, 5]
# n = 2

# [1] --> [2] --> [3] --> [4] --> [5]
# n = 2, so
# LAG             LEAD
# [1] --> [2] --> [3] --> [4] --> [5], lead will be pointing at 3, lag still pointing at 1 (head)

# WHILE LEAD.NEXT != NONE: JUMP EACH POINTER BY 1

# 1 ITERATION: 
#         LAG             LEAD
# [1] --> [2] --> [3] --> [4] --> [5],
# 2 ITERATIONS:
#                 LAG             LEAD
# [1] --> [2] --> [3] --> [4] --> [5],

# we stop here, because lead.next = None and now have figuered out a way to loop through the list one time while also knowing where the nth node from end of the LL is (lagging)
# now simply set lag.next to just lag.next.next, essentially skipping and deleting the n'th node from the LL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        lag = head
        lead = head

        for i in range(n): # jump to the n'th node
            lead = lead.next

        if lead == None: 
            return head.next

        while lead.next is not None: # while lead.next isn't passed the end of the LL, jump lag and lead node by 1
            lag = lag.next
            lead = lead.next

        # at this point, when fast gets to the end, lag whill be just before the n'th node from the end because it's lagging by 1 node (hence the name)

        lag.next = lag.next.next # now just set lag's next to next.next, skipping the n'th node from the end essentially deleting it 

        return head
        
#

