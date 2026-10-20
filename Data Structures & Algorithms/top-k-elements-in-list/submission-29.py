import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        max_length = max(freq.values()) + 1

        code = [[] for i in range(max_length)]

        for key, value in freq.items():
            code[value].append(key)

        res = []
        for i in range(len(code)-1, -1, -1):
            for j in code[i]:
                if k > 0:
                    res.append(j)
                    k-=1
                else:
                    return res
        return res