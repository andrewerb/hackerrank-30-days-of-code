"""Day 18: Queues and Stacks
"""

import sys
from collections import deque

class Solution:
    """ Take a string s. Enqueue s into a queue and push s into a stack.
        If both match up when popped, then s is a palindrome.

        Not bothering to type check/cast for this implementation.
        
        s is composed of lowercase English letters. No need to fix casing.
    """
    # Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = deque()

    def pushCharacter(self, ch):
        """ pushes a character onto stack.
        """
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        """ enqueues a character in queue
        """
        self.queue.append(ch)

    def popCharacter(self):
        """ pops and returns the character at the top of stack
        """
        return self.stack.pop()

    def dequeueCharacter(self):
        """ dequeues and returns the first character in queue
        """
        return self.queue.popleft()

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
