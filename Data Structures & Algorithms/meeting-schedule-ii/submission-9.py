"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [i.start for i in intervals], [i.end for i in intervals]
        start.sort()
        end.sort()
        s, e = 0, 0

        meeting, res = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                meeting += 1
                res = max(res, meeting)
            else:
                e += 1
                meeting -= 1
            res=max(res, meeting)
        
        return res
            





        