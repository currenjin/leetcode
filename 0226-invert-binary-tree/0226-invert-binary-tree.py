class Solution(object):
    def invertTree(self, root):
        if root is None: return root

        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp

        return root