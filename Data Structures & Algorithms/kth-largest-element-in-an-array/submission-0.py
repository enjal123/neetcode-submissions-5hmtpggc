import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nlist = []
        for n in nums:

            nlist.append(-n)
        count = 0
        heapq.heapify(nlist)

        while count < k:
            largest = -heapq.heappop(nlist)
            count +=1 

        return largest