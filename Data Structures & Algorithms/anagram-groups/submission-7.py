class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        freq = defaultdict(list)


        for word in strs:
            signature = [0] * 26
            for char in word:
                signature[ord('a') - ord(char)] += 1

            code = tuple(signature)

            freq[code].append(word)

        return list(freq.values())
