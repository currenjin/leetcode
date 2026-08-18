class Solution(object):
    def maxDepth(self, root):
        if root is None: return 0

        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)

        return max(right_depth, left_depth) + 1