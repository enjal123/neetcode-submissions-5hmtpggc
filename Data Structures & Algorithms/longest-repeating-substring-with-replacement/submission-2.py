class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        

        l, r = 0, 1
        window_size = 0 
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            window_size = max(window_size, r-l+1)
        return window_size
