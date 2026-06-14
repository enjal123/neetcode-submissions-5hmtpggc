class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        return heapq.nlargest(k, freq.keys(), key=freq.get)
