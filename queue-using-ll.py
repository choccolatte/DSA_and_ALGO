class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue (self, element):
        newNode = Node(element)
        if self.back is None:
            self.front = self.back = newNode
            self.length += 1
            return

        self.back.next = newNode
        self.back = newNode
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.back = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end='')
            temp = temp.next
        print()

#creating a queue
myQueue = Queue()

myQueue.enqueue('X')
myQueue.enqueue('Y')
myQueue.enqueue('Z')

print("Queue: ", end="")

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())