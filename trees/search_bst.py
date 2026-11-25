from insert_bst import insert_bst
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def search_bst(root,value):
    if root is None:
        return None
    if root.value==value:
        return root
    if value<root.value:
        return search_bst(root.left,value)
    if value>root.value:
        return search_bst(root.right,value)

root = None

values = [10, 5, 15, 3, 7, 12, 20]

for value in values:
    root = insert_bst(root, value)

result = search_bst(root, 12)

if result is not None:
    print("Found:", result.value)
else:
    print("Not found")


result = search_bst(root, 100)

if result is not None:
    print("Found:", result.value)
else:
    print("Not found")
    
    
                
                
