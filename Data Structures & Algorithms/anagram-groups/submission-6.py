class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:

            sig = [0] * 26

            for char in word:

                sig[ord(char) - ord('a')]+= 1


            sig = tuple(sig)

            groups[sig].append(word)

        
        return list(groups.values())
