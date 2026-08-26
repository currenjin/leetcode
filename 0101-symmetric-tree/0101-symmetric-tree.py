class Solution(object):
    def isSymmetric(self, root):
        
        def isMirror(left, right):
            if right is None and left is None: return True
            if left is None or right is None: return False
            if left.val != right.val: return False

            outer = isMirror(left.left, right.right)
            inner = isMirror(left.right, right.left)

            return outer and inner

        return isMirror(root.left, root.right)