class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left)+count_leaf_nodes(root.right)

a=TreeNode(10)
b=TreeNode(5)
c=TreeNode(8)
d=TreeNode(2)
e=TreeNode(3)

b.left=d
b.right=e
a.left=b
a.right=c

print(count_leaf_nodes(a))
        
