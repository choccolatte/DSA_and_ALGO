stack = [] #empty stack

#push
stack.append('X')
stack.append('Y')
stack.append('Z')
print('Stack: ', stack)

#pop
element = stack.pop()
print('Popped element: ', element)

#Peek
topElement = stack[-1]
print('Peeked element: ', topElement)

#isEmpty
isEmpty = not bool(stack)
print('isEmpty: ', isEmpty)

#size
print("Stack's size: ", len(stack))