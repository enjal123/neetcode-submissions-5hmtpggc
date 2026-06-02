class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:

            # interval completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # interval completely after newInterval
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval

            # overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result