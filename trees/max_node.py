class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def max_node(root):
    if root is None:
        return None
    left_max=max_node(root.left)
    right_max=max_node(root.right)

    values=[root.value]

    if left_max is not None:
        values.append(left_max)

    if right_max is not None:
        values.append(right_max)

    return max(values)

a=TreeNode(10)
b=TreeNode(15)
c=TreeNode(3)
d=TreeNode(7)
e=TreeNode(20)

a.left=b
a.right=c
b.left=d
b.right=e

print(max_node(a))
