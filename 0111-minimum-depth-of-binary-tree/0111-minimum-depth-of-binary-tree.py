class Solution(object):
    def minDepth(self, root):
        if root is None: return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None: return right + 1
        if root.right is None: return left + 1
        
        return min(left, right) + 1