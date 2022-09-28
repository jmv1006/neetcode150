# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)

left = TreeNode(2)
left.left = TreeNode(4)
left.right = TreeNode(5)
root.left = left

right = TreeNode(3)
root.right = right


#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


def dfs(root):
    if not root: return 0

    return 1 + max(dfs(root.left), dfs(root.right))


def diameterOfBinaryTree(root):
    ##find longest path on left
    longest_left = dfs(root.left)

    ##find longest path on right
    longest_right = dfs(root.right)

    ldiamte
    return longest_left + longest_right

diameterOfBinaryTree(TreeNode(3))