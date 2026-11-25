from insert_bst import insert_bst
def __init__(self,value):
    self.value=value
    self.left=None
    self.right=None
def find_min_bst(root):
    if root is None:
        return None
    if root.left is None:
        return root.value

    return find_min_bst(root.left)

root=None
values=[10,5,15,3,7,12,20]

for value in values:
    root=insert_bst(root,value)
    
print("minimum:", find_min_bst(root))
