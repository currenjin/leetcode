class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None: return False

        result = targetSum - root.val
        if root.left is None and root.right is None and result == 0: return True
        
        left = self.hasPathSum(root.left, result)
        right = self.hasPathSum(root.right, result)

        return left or right