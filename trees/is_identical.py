class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def is_identical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    return (
        is_identical(root1.left,root2.left) and is_identical(root1.right,root2.right)
        )
root1=TreeNode(10)
root1.left=TreeNode(8)
root1.right=TreeNode(2)

root2=TreeNode(10)
root2.left=TreeNode(8)
root2.right=TreeNode(2)

root3=TreeNode(10)
root3.right=TreeNode(8)
root3.left=TreeNode(9)


print(is_identical(root1,root2))
print(is_identical(root1,root3))
print(is_identical(None,None))


      





                                                
