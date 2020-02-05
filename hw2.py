## Problem 5
class QueueX:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
## Problem 19
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def slice(self, start, stop):
        item = 0
        current = self.head
        printOut = []
        
        while item != stop:
            if item < start:
                current = current.getNext()
                item += 1
            else:
                printOut.append(current.getData())
                current = current.getNext()
                item += 1
        return printOut
## Problem 22
class Node:
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
class Stack:
     def __init__(self):
         self.head = None

     def isEmpty(self):
         return self.head == None
        
     def push(self, item):
         temp = Node(item)
         temp.setNext(self.head)
         self.head = temp

     def pop(self):
         current = self.head
         while current != None:
             current = current.getNext()
         temp = self.head
         self.head = self.head.next
         popped = temp.data
         return popped

     def peek(self):
         if self.isEmpty():
             return None
         else:
             return self.head.data

     def size(self):
         current = self.head
         count = 0
         while current != None:
             count += 1
             current = current.getNext()
         return count
## Problem 23
class Queue:
    def __init__(self):
        self.front = self.back = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, item):
        temp = Node(item)
        if self.back == None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp
        
    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.back = None
        return temp.data

    def size(self):
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
## Problem 24
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def addFront(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
        if self.size() == 1:
            self.tail = newNode
            self.temp = self.tail
        self.count += 1
        
    def addRear(self, item):
        last = None
        current = self.head
        while current != None:
            last = current
            current = current.getNext()
        self.tail = last
        if self.size() == 0:
            new = Node(item)           
            self.tail = new                 
            self.temp = self.tail               
            self.head = self.tail
        else:
            new = Node(item)
            self.tail.setNext(new)
        self.count += 1
        
    def removeFront(self):
        poppedHead = self.head
        self.head = self.head.getNext()
        self.count -= 1
        return poppedHead.getData()

    def removeRear(self):
        last = None
        popped = self.tail
        current = self.head
        
        while current.getNext() != None:
            last = current
            current = current.getNext()
        
        if self.count == 1:
            self.count -= 1
            return popped.getData()
        else:
            last.setNext(None)
            self.tail = last
            self.count -= 1
        return popped.getData()
    
    def size(self):
        return self.count

## Question 6 (Problem 27)
class Node2:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.back = None
        
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getBack(self):
        return self.back
    
    def setBack(self, newback):
        self.back = newback

class Deque2:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addFront(self, item):
        temp = Node2(item)
        current = self.head
        last = None

        temp.setNext(self.head)
        if self.head != None:
            self.head.setBack(temp)
        self.head = temp

        while current != None:
            last = current
            current = current.getNext()
        self.tail = last
        
    def addRear(self, item):
        temp = Node2(item)
        last = None
        current = self.head
        while current != None:
            last = current
            current = current.getNext()

        temp.setBack(last)
        
        if last == None:
            self.head = temp
        else:
            last.setNext(temp)
        self.tail = temp
        
    def removeFront(self):
        if self.size() < 2:
            self.head = None
        else:
            self.head = self.head.getNext()
            self.head.setBack(None)

    def removeRear(self):
        current = self.head
        last = None
        if current != None:
            while current.getNext() != None:
                last = current
                current = current.getNext()
        if self.size() <= 1:
            self.head = None
        else:
            last.setNext(None)
            self.tail = self.tail.getBack()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
