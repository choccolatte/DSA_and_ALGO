class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

#creating a new queue
newqueue = Queue()

newqueue.enqueue('o')
newqueue.enqueue('p')
newqueue.enqueue('q')
print('Queue enqueued: ', newqueue.queue)

print("Queue dequeued: ", newqueue.dequeue())

print("Queue peeked: ", newqueue.peek())

print("Queue isEmpty: ", newqueue.isEmpty())

print("Queue size: ", newqueue.size())