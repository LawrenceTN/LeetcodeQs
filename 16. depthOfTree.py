# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# finding the max depth of a binary tree is finding the longest path from root to farthest leaf node

class Solution(object):
    def maxDepth(self, root):
        # if root is empty: return 0
        if root is None:
            return 0
        # we can use recursion to figure out if their are child nodes for the left & right side of the tree, don't forget to add `self` for function calls in classes
        leftSide = self.maxDepth(root.left)
        rightSide = self.maxDepth(root.right)
 
        # when root eventually is none after traversing down for each side it'll maintain the same values (static) through recursion, then you add 1 for the innate level due to the root
        return max(leftSide, rightSide)+1