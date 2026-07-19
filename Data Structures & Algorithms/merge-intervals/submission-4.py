class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()

        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= current[1]:
                current[1] = max(current[1], interval[1])
            else:
                res.append(current)
                current = interval

        res.append(current)

        return res