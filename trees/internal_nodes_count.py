class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def internal_nodes_count(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1+internal_nodes_count(root.left)+internal_nodes_count(root.right)

a=TreeNode(10)
b=TreeNode(5)
c=TreeNode(8)
d=TreeNode(2)
e=TreeNode(3)

b.left=d
b.right=e
a.left=b
a.right=c

print(internal_nodes_count(a))
        
