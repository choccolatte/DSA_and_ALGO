class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty:
            return 'Stack is Empty'
        return self.stack.pop()

    def peek(self):
        if self.isEmpty:
            print('Stack is empty')
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#creating a new stack
newStack = Stack()

newStack.push('O')
newStack.push('P')
newStack.push('Q')

print("Stack: ", newStack.stack)

print("Pop: ", newStack.pop())

print("Peek: ", newStack.peek())

print("isEmpty: ", newStack.isEmpty())

print("Size: ", newStack.size())