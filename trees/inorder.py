class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)

a=TreeNode("A")
b=TreeNode("B")
c=TreeNode("C")
d=TreeNode("D")
e=TreeNode("E")

b.left=d
b.right=e
a.left=b
a.right=c

inorder(a)
