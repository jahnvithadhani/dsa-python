class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def min_node(root):
    if root is None:
        return None
    left_min=min_node(root.left)
    right_min=min_node(root.right)

    values=[root.value]

    if left_min is not None:
        values.append(left_min)
    if right_min is not None:
        values.append(right_min)
    return min(values)
a=TreeNode(10)
b=TreeNode(3)
c=TreeNode(6)
d=TreeNode(7)
e=TreeNode(2)

a.left=b
a.right=c
b.left=d
b.right=e

print(min_node(a))

