'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-02-01 01:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-02-01 01:14:30

@Title : Stack datastructures

'''

from linkedlistclass import LinkedList

class Queue:
    def __init__(self):
        self.queue=LinkedList()

    def enqueue(self,val):
        self.queue.push((val))

    def dequeue(self):
        if self.queue.isempty():
            return -1
        if not self.queue.head.next:
            val=self.queue.head.val
            self.queue.head=self.queue.head.next
            return val
        curr=self.queue.head
        while curr:
            if curr.next is not None and curr.next.next is None:
                val=curr.next.val
                curr.next=curr.next.next
            curr=curr.next
        return val


    def isempty(self):
        True if self.queue.isempty() else False

    def show(self):
        self.queue.print()

    def length(self):
        return self.queue.length

if __name__=="__main__":
    q=  Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.show()
    q.dequeue()
    q.dequeue()
    q.show()
    q.dequeue()
    q.show()
    q.dequeue()
    q.show()

