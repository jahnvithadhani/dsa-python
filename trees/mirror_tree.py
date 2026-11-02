class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def mirror_tree(root):
    if root is None:
        return None
    root.left,root.right=root.right,root.left

    mirror_tree(root.left)
    mirror_tree(root.right)

    return root

a=TreeNode(10)
b=TreeNode(8)
c=TreeNode(5)
d=TreeNode(2)
e=TreeNode(3)

a.right=c
a.left=b
b.left=d
b.right=e

print(mirror_tree(a))
