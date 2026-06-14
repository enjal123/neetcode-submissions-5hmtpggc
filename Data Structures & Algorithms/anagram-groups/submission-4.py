class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        seen = defaultdict(list)
        for words in strs:
            code = [0] * 26
        
            for char in words:
                code[ord(char) - ord('a')] += 1


            codex = tuple(code)

            seen[codex].append(words)

        
        return list(seen.values())
