# Given two integers a and b, return the sum of the two integers without using the operators + and -.

a = 1
b = 2

# 0001
# 0010
# ----
# 0011 = 3

#what if carry?

# 0011 3
# 0101 5
# ----
# 1000 (3 carries)

# how do you add numbers? use XOR, 1+1=0, 0+1=1, 1+0=1, 0+0=0
# how do you find the carry? use AND, 1+1=1 
# ok, you found carry, but now what? carry goes to the left, so then you shift left using << and restart the process again until carry = 0


def getSum(a, b):
    while b != 0: # until carry is 0
        carry = (a&b)<<1
        a = a^b
        b = carry
    print(a)

print(getSum(a, b))