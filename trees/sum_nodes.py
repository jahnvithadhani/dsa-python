class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def sum_nodes(root):
    if root is None:
        return 0
    return root.value + sum_nodes(root.left)+ sum_nodes(root.right)
a=TreeNode(10)
b=TreeNode(5)
c=TreeNode(8)
d=TreeNode(2)
e=TreeNode(3)

a.left=b
a.right=c
b.left=d
b.right=e

print(sum_nodes(a))
        
