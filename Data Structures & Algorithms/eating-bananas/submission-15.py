class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        left = 1
        right = max(piles)

        res = right

        while left <= right:

            rate = (left + right) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/rate)
            if totalTime <= h:
                res = rate
                right = rate - 1
            else:
                left = rate + 1

        return res
                