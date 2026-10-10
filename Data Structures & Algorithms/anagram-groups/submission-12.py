class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for word in strs:
            sign = [0] * 26
            for char in word:
                sign[ord('a') - ord(char)] += 1

            sign_tup = tuple(sign)

            groups[sign_tup].append(word)


        return list(groups.values())


