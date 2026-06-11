class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS, countT = {}, {}

        for n in s:
            if n not in countS:
                countS[n] = 1
            else:
                countS[n] += 1

        for j in t:
            if j not in countT:
                countT[j] = 1
            else:
                countT[j] += 1

        return countS == countT