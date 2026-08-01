class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        expected = sum(range(length + 1))
        actual = sum(nums)

        return expected - actual
        