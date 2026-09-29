class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        

from collections import deque
def level_order(root):
    if root is None:
        return
    queue=deque([root])

    while queue:
        node=queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

b.left=d
b.right=e
a.left=b
a.right=c

level_order(a)
