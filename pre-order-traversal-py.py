def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end = ", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)