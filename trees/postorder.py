class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value)

a=TreeNode("A")
b=TreeNode("B")
c=TreeNode("C")
d=TreeNode("D")
e=TreeNode("E")

b.left=d
b.right=e
a.left=b
a.right=c

postorder(a)
