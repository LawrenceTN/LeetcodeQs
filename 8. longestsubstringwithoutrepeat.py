# Given a string s, find the length of the longest substring without repeating characters.

s = "abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"

# incomplete, still getting some errors...

# iterate through string, adding each letter to a set + count if letter doesnt already exist in set
# sets cant hold duplicate values

def lengthOfLongestSubstring(s):
    count = 1
    highest_count = 0
    mySet = set()
    for letter in s:
        if letter in mySet:
            count = 1
            mySet.clear()
        mySet.add(letter)
        if count > highest_count:
            highest_count = count
        count += 1
    return highest_count 

print(lengthOfLongestSubstring(s))
print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))