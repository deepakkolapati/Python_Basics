'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-31 01:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-31 01:14:30

@Title : Linked List datastructures
'''


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def push(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def pop(self):
        if self.isempty():
            return -1
        val = self.head.val
        self.head = self.head.next
        self.length-=1
        return val

    def print(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print(None)

    def isempty(self):
        return True if self.length==0 else False

    def reverse(self):
        prev = None
        curr=None
        next=self.head
        while next:
                curr=next
                next=next.next
                curr.next=prev
                prev=curr
        self.head=curr


if __name__=="__main__":
    l1=LinkedList()
    l1.push(10)
    l1.push(20)
    l1.push(30)
    l1.push(40)
    l1.print()
    l1.pop()
    l1.pop()
    l1.print()
    l1.push(50)
    l1.push(35)
    l1.print()
    l1.reverse()
    l1.print()


