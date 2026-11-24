class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def diameter(root):
    def helper(node):
        if node is None:
            return -1,0

        left_height,left_diameter = helper(node.left)
        right_height,right_diameter=helper(node.right)

        height=max(left_height,right_height)+1

        diameter_through_node=left_height +right_height +2

        diameter=max(
            diameter_through_node,left_diameter,right_diameter
            )
        return height,diameter
    
    return helper(root)[1]

root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(8)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(3)

print(diameter(root1))


        
