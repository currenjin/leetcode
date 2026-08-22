class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return p.val == q.val and left and right