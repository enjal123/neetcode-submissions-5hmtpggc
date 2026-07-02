class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums)+1)]

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) -1, 0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
