"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        count, maxCount = 0, 0
        start_i, end_i = 0, 0
        while start_i < len(start):
            if start[start_i] < end[end_i]:
                start_i += 1
                count += 1
                maxCount = max(maxCount, count)
            else:
                end_i += 1
                count -= 1
        return maxCount