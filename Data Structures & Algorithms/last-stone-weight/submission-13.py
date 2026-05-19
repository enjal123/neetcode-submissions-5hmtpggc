import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n_stones = []

        for s in stones:
            n_stones.append(-s)

        heapq.heapify(n_stones)


        while len(n_stones) > 1:
            x = -heapq.heappop(n_stones)
            y = -heapq.heappop(n_stones)
 
            if x != y:
                heapq.heappush(n_stones, -(x - y))
        if n_stones:
            return -n_stones[0]

        return 0 