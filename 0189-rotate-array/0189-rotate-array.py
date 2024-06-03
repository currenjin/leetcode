class Solution(object):
    def rotate(self, nums, k):
        count = k % len(nums)
        length = len(nums)
        
        original = nums[0:length - count]
        del nums[0:length - count]
        nums += original