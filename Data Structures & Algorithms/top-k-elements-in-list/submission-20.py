import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        max_length = max((freq.values()))
        freq_array = [[] for _ in range(max_length+1)]
        res = []

        for value, count in freq.items():
            freq_array[count].append(value)

        for i in range(len(freq_array)-1, -1, -1):
            for bucket in freq_array[i]:
                res.append(bucket)
                if len(res) == k:
                    return res

