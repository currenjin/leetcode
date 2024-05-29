class Solution(object):
    def majorityElement(self, nums):
        setNums = list(set(nums))
        major = setNums[0]
        
        for i in setNums:
            if(nums.count(i) > nums.count(major)):
                major = i
                
        return major
        