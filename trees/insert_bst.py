class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
def insert_bst(root,value):
    if root is None:
        return TreeNode(value)
    if value<root.value:
        root.left=insert_bst(root.left,value)
    elif value>root.value:
        root.right=insert_bst(root.right,value)
    return root
def print_tree(root):
    if root is None:
        return

    print(root.value,end=" ")
    print_tree(root.left)
    print_tree(root.right)

root=None

values=[10,5,15,3,7,12,20]

for value in values:
    root=insert_bst(root,value)
print("preorder traversal:")
print_tree(root)
print()
