from insert_bst import insert_bst
def delete_bst(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete_bst(root.left, value)

    elif value > root.value:
        root.right = delete_bst(root.right, value)

    else:
        # Case 1: No children
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = root.right

        while successor.left is not None:
            successor = successor.left

        root.value = successor.value
        root.right = delete_bst(root.right, successor.value)

    return root
def print_tree(root):
    if root is None:
        return

    print(root.value, end=" ")
    print_tree(root.left)
    print_tree(root.right)

root = None


values = [10, 5, 15, 3, 7, 12, 20]

for value in values:
    root = insert_bst(root, value)

print("Before deletion:")
print_tree(root)

root = delete_bst(root, 10)

print("\nAfter deleting 10:")
print_tree(root)


    
