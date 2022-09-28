# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)

right = TreeNode(20)
right.left = TreeNode(15)
right.right = TreeNode(7)
right.left.left = TreeNode(12)

root.right = right

root2 = TreeNode(1)
dosnode = TreeNode(2)
root2.right = dosnode
dosnode.left = TreeNode(3)
#height = number of edges between node and its furthest leaf

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(3)
root3.left.left.left = TreeNode(4)
root3.right = TreeNode(2)
root3.right.right = TreeNode(3)
root3.right.right.right = TreeNode(4)

def calculateHeight(root):
    if not root: return 0

    return 1 + max(calculateHeight(root.left), calculateHeight(root.right))

def isBalanced(root):
    if not root: return True

    heightLeft = calculateHeight(root.left)
    heightRight = calculateHeight(root.right)


    if(calculateHeight(root.left) - calculateHeight(root.right) <= 1):
        return True
    else: return False







print(isBalanced(root3))