class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def is_mirror(left,right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.value!=right.value:
        return False
    return (
        is_mirror(left.left,right.right) and is_mirror(left.right,right.left)
        )
def is_symmetric(root):
    if root is None:
        return True
    return is_mirror(root.left,root.right)
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.right.right = TreeNode(3)

print(is_symmetric(root1))






    
    
                   

