class Solution(object):
    def removeDuplicates(self, nums):
        for i in nums:
            while(nums.count(i) > 1):
                nums.remove(i)
        
        sorted(nums)