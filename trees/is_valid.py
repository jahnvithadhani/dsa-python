from insert_bst import insert_bst
def check_bst(node,min_value,max_value):
    if node is None:
        return True
    if node.value<=min_value:
        return False
    if node.value>=max_value:
        return False

    left_valid=check_bst(node.left,min_value,node.value)
    right_valid=check_bst(node.right,node.value,max_value)

    return left_valid and right_valid
def is_valid(root):
    return check_bst(root,float('-inf'),float('inf'))

root=None
values=[10,5,15,3,7,12,20]
for value in values:
    root=insert_bst(root,value)

print("test 1:", is_valid(root))

root = None
values = [10, 5, 15, 12]

for value in values:
    root = insert_bst(root, value)

root.left.right = insert_bst(None, 12)

print("Test 2:", is_valid(root))
