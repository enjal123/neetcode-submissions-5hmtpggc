class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}
        count2 = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        if count == count2:
            return True
        else:
            return False

        
