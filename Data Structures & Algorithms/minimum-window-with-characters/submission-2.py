class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""
        need, window = {}, {}

        for char in t:
            need[char] = 1 + need.get(char,0)

        need_count = len(need)
        have_count = 0
        l = 0
        res, resLen = [-1,-1], float("infinity")
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in need and window[char] == need[char]:
                have_count += 1
            
            while have_count == need_count:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have_count -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        