class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)

        for words in strs:

            key = [0] * 26

            for char in words:
                key[ord(char) - ord('a')] += 1

            code = tuple(key)

            seen[code].append(words)

        
        return list(seen.values())