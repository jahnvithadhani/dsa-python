class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
def count_nodes(root):
    if root is None:
        return 0
    return 1+ count_nodes(root.left)+count_nodes(root.right)

a=TreeNode("A")
b=TreeNode("B")
c=TreeNode("C")
d=TreeNode("D")
e=TreeNode("E")

b.left=d
b.right=e
a.left=b
a.right=c

print(count_nodes(a))













            
    
