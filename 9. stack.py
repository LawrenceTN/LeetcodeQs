# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# min(), which returns the min value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

# a stack is a data structure that has the following commands up above
# basically, a pringles can, where the chips are elements. you can't remove the chips that are below the top one
# LIFO


class Stack:
    def __init__(self):
        self.stack = []
        self.min = float('inf') # sets min to infinity, used to compare with any number pushed into stack
    
    def push(self, value: int) -> None:
        self.stack.append((value, self.max)) # append the pair of added value & max
        self.min = min(self.min, value) # compares min and value, sets min to what's less
        
    def pop(self) -> None:
        self.min = self.stack[-1][1] # python supports negative indexing, so this returns the LAST pair, 2nd element, so set min to prev low value and then pop
        self.stack.pop()

    def getMin(self) -> None:
        return self.min