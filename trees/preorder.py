class treenode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def preorder(root):
    if root is None:
        return

    print(root.value)
    preorder(root.left)
    preorder(root.right)

a=treenode("A")
b=treenode("B")
c=treenode("C")
d=treenode("D")
e=treenode("E")

b.left=d
b.right=e
a.left=b
a.right=c

preorder(a)
