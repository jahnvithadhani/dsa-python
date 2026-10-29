class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def search_tree(root,target):
    if root is None:
        return False

    if root.value==target:
        return True

    return search_tree(root.left,target) or search_tree(root.right,target)
a=TreeNode(5)
b=TreeNode(8)
c=TreeNode(12)
d=TreeNode(7)
e=TreeNode(19)

a.left=b
a.right=c
b.left=d
b.right=e

print(search_tree(a,12))
