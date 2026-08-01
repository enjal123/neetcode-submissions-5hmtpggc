class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            # Shrink window from the left until the duplicate is removed
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # Add current character and update max length
            seen.add(s[r])
            longest = max(longest, r - l + 1)
            
        return longest