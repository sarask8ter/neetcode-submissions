class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        endMin = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < endMin:
                res += 1
                endMin = min(intervals[i][1], endMin)
            else:
                endMin = intervals[i][1]
        
        return res
        