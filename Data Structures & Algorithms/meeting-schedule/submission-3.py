"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        index = 0
        intervals = sorted(intervals, key=lambda i: i.start)
        for i in range(len(intervals)-1):
            current = intervals[i]
            next_meeting = intervals[i+1]

            if current.start > current.end:
                return False
            
            if current.start > next_meeting.start and current.end < next_meeting.start:
                return False

            if current.end > next_meeting.start:
                return False
            
            if next_meeting.start > current.start and next_meeting.start < current.end:
                return False
        
        return True

