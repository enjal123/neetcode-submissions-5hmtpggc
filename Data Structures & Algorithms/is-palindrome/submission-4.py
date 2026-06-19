import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        left = 0
        right = len(s) -1
        s = s.lower()

        while left < right:
            if s[left] == s[right]:
                left +=1 
                right -= 1
                continue
            else:
                return False
        
        return True