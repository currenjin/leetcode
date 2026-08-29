class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None: return False
        if targetSum - root.val == 0 and root.left is None and root.right is None: return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)