class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

newStack = Stack()
newStack.push('M')
newStack.push('N')
newStack.push('O')

print("Pop: ", newStack.pop())
print("Peek: ", newStack.peek())
print("isEmpty: ", newStack.isEmpty())
print("Size: ", newStack.stackSize())