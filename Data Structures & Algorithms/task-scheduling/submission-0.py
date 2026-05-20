from _heapq import heapify
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = {}

        for c in tasks:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        print(count)

        max_heap = []

        for i in count.values():
            max_heap.append(-i)

        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1

                if cnt < 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] == time:
                ready, _ = cooldown.popleft()
                heapq.heappush(max_heap, ready)

        return time



