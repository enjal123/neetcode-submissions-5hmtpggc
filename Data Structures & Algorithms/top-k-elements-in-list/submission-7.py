class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [ [] for _ in range(len(nums)+ 1)]
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for n, f in freq.items():
            buckets[f].append(n)
        
        res = []

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k:
                    return res
