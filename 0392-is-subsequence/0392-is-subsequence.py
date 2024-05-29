class Solution(object):
    def isSubsequence(self, s, t):
        count = 0
        first = 0
        second = 0
        
        while(first < len(s)):
            if(second > len(t) - 1):
                break
                
            if(s[first] == t[second]):
                first += 1
                count += 1
                
            second += 1
        
        return count == len(s)