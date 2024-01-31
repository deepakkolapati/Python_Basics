'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-31 01:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-31 01:14:30

@Title : Stack datastructures

'''


from linkedlistclass import Node,LinkedList

class Stack:
    def __init__(self):
        self.stack=LinkedList()

    def push(self,val):
        self.stack.push(val)

    def pop(self):
        val=self.stack.pop()
        return val

    def isempty(self):
        return self.stack.isempty()

    def length(self):
        return self.stack.length

    def print(self):
        self.stack.print()
if __name__=="__main__":
    s=Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.print()
    s.pop()
    s.pop()
    s.print()