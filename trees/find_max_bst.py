from insert_bst import insert_bst
def find_max_bst(root):
    if root is None:
        return None
    if root.right is None:
        return root.value

    return find_max_bst(root.right)
root=None

values=[10,3,5,7,15,12,20]
for value in values:
    root=insert_bst(root,value)
print("maximum:",find_max_bst(root))
