# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# n = 00000000000000000000000000001011

# for this, we are going to iterate through the given value with a for loop (max 32 times), and check if anding each value with 1 is equal to 1
# an AND operator can only result in 1 if the operands are both 1 (1&1 == 1)
# if it is 1, increment our counter
# if not, right shift our value by itself and 1, so that we can move onto the next value

def hammingWeight(n):
    count = 0
    for _ in range(32):
        if n&1 == 1:
            count += 1
        n=n>>1
    print(count)

hammingWeight(n)