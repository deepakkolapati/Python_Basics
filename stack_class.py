'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-31 01:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-31 01:14:30

@Title : Stack datastructures

'''



class Stack:

    def __init__(self):
        self.stack=[]
        self.top=-1

    def push(self,item):
        self.stack.append(item)
        self.top+=1

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return
        item=self.stack.pop()
        self.top-=1
        return item
    
    def isempty(self):
        return True if self.top==-1 else False
    
    def __str__(self):
        return f"{self.stack}"
    
if __name__=="__main__":
    s1=Stack()
    s1.push(20)
    s1.push(40)
    s1.push(30)
    s1.push(50)
    s1.push(10)
    print(s1)
    s1.pop()
    s1.pop()
    print(s1)
    s1.push(-2)
    print(s1)
    
