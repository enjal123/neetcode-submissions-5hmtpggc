import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        ignore = ['?', " ",".", ",", "'", ":", ";", "/", "[", "]"]

        s = s.lower()
        w = []

        for char in s:
            if char not in ignore:
                w.append(char)
            else:
                continue

        if w == []:
            return True
        print(w)

        l = 0 
        r = len(w) - 1

        while l <= r:
            left_letter = w[l]
            right_letter = w[r]

            if left_letter == right_letter:
                l += 1
                r -= 1
                if l >= r:
                    return True
                continue
            return False
            

        return False