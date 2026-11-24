class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
def is_balanced(root):
    def helper(node):
        if node is None:
            return -1, True

        left_height, left_balanced = helper(node.left)
        right_height, right_balanced = helper(node.right)

        height = max(left_height, right_height) + 1

        if not left_balanced or not right_balanced:
            return height, False

        difference = abs(left_height - right_height)

        if difference > 1:
            return height, False

        return height, True

    return helper(root)[1]

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(is_balanced(root1))
