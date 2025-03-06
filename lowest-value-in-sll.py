class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(702311)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(70)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('Lowest valie in the linked list is: ', findLowestValue(node1))
