def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        #Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        #Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)
    return node