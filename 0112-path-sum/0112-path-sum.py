class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None: return False
        
        remain = targetSum - root.val
        if remain == 0 and root.left is None and root.right is None: return True
        
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)