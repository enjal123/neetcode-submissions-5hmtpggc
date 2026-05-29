import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        count = 0
        max_heap = []

        for num, fre in freq.items():
            max_heap.append((-fre, num))

        heapq.heapify(max_heap)

        res = []
        while count < k:
            curr, num = heapq.heappop(max_heap)

            res.append(num)
            count += 1

        return res