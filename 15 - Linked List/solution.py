# Day 15: Linked List
__author__ = "Andrew Erb"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    ## user-made
    def insert(self,head,data): 
    #Complete this method
        """This is trying to place one data entry at a time.
        If head is emoty, set it. Otherwise, check for a free child Node position.
        """
        if head == None:
            head = Node(data)
        else:
            current = head
            while current:
                if current.next:
                    current = current.next
                else:
                    current.next = Node(data)
                    current = None
        return head


## end of user-made
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	
