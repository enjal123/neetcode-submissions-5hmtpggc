class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for num, f in freq.items(): # (key: value)
            buckets[f].append(num)

        res = []

        for top_k in range(len(buckets)-1, 0, -1):
            for n in buckets[top_k]:
                res.append(n)
                if len(res) == k:
                    return res