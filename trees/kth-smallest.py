import heapq

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

left = TreeNode(3)

root.left = left

left.right = TreeNode(4)

leftchild = TreeNode(2)
leftchild.left = TreeNode(1)

left.left = leftchild


right = TreeNode(6)
root.right = right


root2 = TreeNode(3)
root2.right = TreeNode(4)

root2left = TreeNode(1)
root2left.right = TreeNode(2)

root2.left = root2left

def kthSmallest(root, k):
    heap = []

    def dfs(root):
        if not root: return None

        dfs(root.left)
        heapq.heappush(heap, root.val)
        dfs(root.right)
    
    dfs(root)

    pops = 0

    while pops < k - 1:
        heapq.heappop(heap)
        pops += 1
    
    return heap[0]

print(kthSmallest(root2, 1))