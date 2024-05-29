class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        result = []
        
        while(left < right):
            total = numbers[left] + numbers[right]
            
            if(total > target):
                right -= 1
                continue
                
            if(total < target):
                left += 1
                continue
            
            result.append(left + 1)
            result.append(right + 1)
            break
            
        return result