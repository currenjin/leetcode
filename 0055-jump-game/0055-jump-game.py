class Solution(object):
    def canJump(self, nums):
        index = 0
        for i in nums:
            if index < 0: return False
            index = max(i, index) - 1
        return True