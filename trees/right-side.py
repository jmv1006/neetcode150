

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
left = TreeNode(2)
left.right = TreeNode(5)
root.left = left

right = TreeNode(3)
right.right = TreeNode(4)
root.right = right


##from each level we want the rightmost node

def rightSideView(root):
    if not root: return []
    res = []
    
    queue = []
    queue.append(root)

    while queue:
        rightSide = None
        qlen = len(queue)

        print(queue)
        
        for i in range(qlen):
            node = queue.pop(0)
            if node:
                rightSide = node
                queue.append(node.left)
                queue.append(node.right)
        
        if rightSide: res.append(rightSide.val)
    
    return res



    
rightSideView(root)