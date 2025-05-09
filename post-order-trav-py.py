def postOrderTraversal(node):
    if node is None:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end = ", ")