class Solution(object):
    def minDepth(self, root):
        if root is None: return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left == 0 or right == 0: return max(left, right) + 1
        return min(left, right) + 1