class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        intervals.sort()
        res = []
        current = intervals[0]
        count = 0

        for interval in intervals[1:]:
            if interval[0] < current[1]:
                count +=1
                current[1] = min(current[1], interval[1])
            else:
                current = interval
        
        return count