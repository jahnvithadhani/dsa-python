class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def height(root):
    if root is None:
        return -1

    return 1 + max(height(root.left),height(root.right))


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

b.left = d
b.right = e
a.left = b
a.right = c

print(height(a))



    
        
        
