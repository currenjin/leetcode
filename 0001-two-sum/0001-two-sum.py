class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in nums_dict:
                return [nums_dict[need], i]
            
            nums_dict[num] = i
