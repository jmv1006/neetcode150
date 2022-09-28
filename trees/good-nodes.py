# Definition for a binary tree node.
from audioop import maxpp
from cmath import inf


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(1, left=TreeNode(3))

right = TreeNode(4)
right.left = TreeNode(1)
right.right = TreeNode(5)

root.right = right

root2 = TreeNode(3)

left2 = TreeNode(3)
left2.left = TreeNode(4)
left2.right = TreeNode(2)

root2.left = left2

root3 = TreeNode(2)
root3r = TreeNode(4)
root3r.left = TreeNode(10)
root3r.right = TreeNode(8, right=TreeNode(4))
root3.right = root3r
## Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
## in other words, x.val must be the SMALLEST value in a given path

def goodNodes(root):
    good_nodes = []

    def dfs(root, maxVal):
        if not root: return

        if root.val > maxVal or root.val == maxVal:
            maxVal = root.val
            good_nodes.append(root.val)

        dfs(root.left, maxVal)
        dfs(root.right, maxVal)
    
    dfs(root, root.val)
    return len(good_nodes)

print(goodNodes(root))