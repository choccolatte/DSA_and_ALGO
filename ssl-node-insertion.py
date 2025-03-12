class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
    print('null')

def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(70)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(702311)

node1.next = node2
node2.next = node3
node3.next = node4

print('Original list: ')
traverseAndPrint(node1)

#inserting a new node with value = 9899 at position 4
newNode = Node(9899)
node1 = insertNodeAtPosition(node1, newNode, 4)

print('\nAfter inserting: ')
traverseAndPrint(node1)