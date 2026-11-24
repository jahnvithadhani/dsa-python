
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root

    if left is not None:
        return left

    return right



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)


p = root.left.left
q = root.left.right
print(lowest_common_ancestor(root, p, q).value)
