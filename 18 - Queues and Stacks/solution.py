"""Day 18: Queues and Stacks
"""

import sys

class Solution:
    """ Take a string s. Enqueue s into a queue and push s into a stack.
        If both match up when popped, then s is a palindrome.

        Not bothering to type check/cast for this implementation.
    """
    # Write your code here
    def __init__(self):
        self.stack = None
        self.queue = None

    def pushCharacter(self, ch):
        pass

    def enqueueCharacter(self, ch):
        pass

    def popCharacter(self):
        pass

    def dequeueCharacter(self):
        pass

    # end of custom code
###########################################

# read the string s
s = input()
#Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
