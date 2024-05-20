import re

class Solution(object):
    def isPalindrome(self, s):
        target = re.sub('[^0-9a-zA-Z]', '', s.lower())
        reversedTarget = ''.join(reversed(list(target)))

        return target == reversedTarget