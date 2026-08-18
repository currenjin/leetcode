class Solution(object):
    def isSameTree(self, p, q):
        if q is None and p is None: return True
        if q is None or p is None: return False

        if q.val != p.val: return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        
        return isLeftSame and isRightSame