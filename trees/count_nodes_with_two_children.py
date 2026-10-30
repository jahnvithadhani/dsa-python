class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def count_nodes_with_two_children(root):
    if root is None:
        return 0
    count=0

    if root.left is not None and root.right is not None:
        count=1
    return count+count_nodes_with_two_children(root.left)+count_nodes_with_two_children(root.right)

a=TreeNode(10)
b=TreeNode(5)
c=TreeNode(8)
d=TreeNode(2)
e=TreeNode(3)

a.left=b
a.right=c
b.left=d
b.right=e

print(count_nodes_with_two_children(a))
   

                
