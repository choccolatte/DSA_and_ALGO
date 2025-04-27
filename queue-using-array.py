queue = []

#enqueue
queue.append('X')
queue.append('Y')
queue.append('Z')
print('Queue: ', queue)

#dequeue
element = queue.pop(1)
print('Dequeued element: ', element)

#peek
frontElement = queue[0]
print('Peek result: ', frontElement)

#isEmpty
isEmpty = not bool(queue)
print('isEmpty result: ', isEmpty)

#size
print("Queue's Size:" , len(queue))