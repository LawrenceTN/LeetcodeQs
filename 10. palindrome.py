# Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

# this question can be solved using a variety of methods in python, but here are two that i thought of

def isPalindrome1(s):

    reverse = ""

    for letter in s[::-1]: # this is the way to iterate over a string/list in reverse order, then just add it to itself to build the world
        reverse += letter

    print(reverse)
    
    if reverse == s:
        return True
    else:
        return False

# we can also take a string and then simply use the built-in reversed method for strings

def isPalindrome2(s):
    reverse = ''.join(reversed(s))
    print(reverse)

    if reverse == s:
        return True
    else:
        return False
    
word1 = "japan"
word2 = "racecar"

print(isPalindrome1(word1))
print(isPalindrome1(word2))

print(isPalindrome2(word1))
print(isPalindrome2(word2))