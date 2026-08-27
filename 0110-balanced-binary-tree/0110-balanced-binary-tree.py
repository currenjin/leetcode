class Solution(object):
    def isBalanced(self, root):
        def calHeight(root):
            if root is None: return 0

            left = calHeight(root.left)
            right = calHeight(root.right)

            if left == -1 or right == -1: return -1
            if abs(left - right) > 1: return -1

            return max(left, right) + 1

        return calHeight(root) != -1