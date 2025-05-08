def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end = ",")
    inOrderTraversal(node.right)