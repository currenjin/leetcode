class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while(left < right):
            total = numbers[left] + numbers[right]
            
            if(total == target):
                return [left + 1, right + 1]
            
            if(total > target):
                right -= 1
                continue
                
            if(total < target):
                left += 1
                continue
