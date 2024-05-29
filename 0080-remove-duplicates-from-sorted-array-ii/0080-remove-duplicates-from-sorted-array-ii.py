class Solution(object):
    def removeDuplicates(self, nums):
        for i in nums:
            while(nums.count(i) > 2):
                nums.remove(i)