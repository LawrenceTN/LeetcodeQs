# Given a simple expression tree, consisting of basic binary operators i.e., + , – ,* and / and some integers, evaluate the expression tree.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5

# you should return 45, as it is (3+2) * (4+5)

# to solve this, let's create our definition of a node used to build the tree

class Node:
    def __init__ (self, value):
        self.data = value
        self.left = None
        self.right = None
    
def evaluate(root): # top node, work way down
    
    # if empty tree,
    if root is None:
        return 0
    
    # how do we go down each side of the tree to collet the numbers values, when we know that the leaf nodes are the numerical values

    leftSum = evaluate(root.left)
    rightSum = evaluate(root.right)

    #so the node's data for math operation are non-leaf nodes under the root

    if root.data == '+':
        return leftSum + rightSum
    elif root.data == '-':
        return leftSum - rightSum
    elif root.data == '*':
        return leftSum * rightSum
    else: # division
        return leftSum / rightSum
    


    



