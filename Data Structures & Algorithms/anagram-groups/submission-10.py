class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = defaultdict(list)

        for word in strs:
            keys = [0] * 26
            for char in word:
                keys[ord(char) - ord('a')] += 1

                
            code = tuple(keys) 

            freq[code].append(word)

        return list(freq.values())