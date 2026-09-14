"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        e=s=0
        res=meeting=0
        start, end = [i.start for i in intervals], [i.end for i in intervals]
        start.sort()
        end.sort()

        while s < len(intervals):
            if start[s] < end[e]:
                meeting += 1
                s += 1
            else:
                meeting -= 1
                e += 1
            
            res = max(res, meeting)
        
        return res
        