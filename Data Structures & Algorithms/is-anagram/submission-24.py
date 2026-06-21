class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS = {}
        countT = {}

        for i in s:
            if i not in countS:
                countS[i] = 1
            else:
                countS[i] += 1

        for j in t:
            if j not in countT:
                countT[j] = 1
            else:
                countT[j] += 1

        return countS == countT
            
            