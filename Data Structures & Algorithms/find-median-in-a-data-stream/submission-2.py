class MedianFinder:

    def __init__(self):
        self.maxH, self.minH = [], []

    def addNum(self, num: int) -> None:
        if self.maxH and num > self.maxH[0]:
            heapq.heappush(self.maxH, num)
        else:
            heapq.heappush(self.minH, -1 * num)
        
        if len(self.maxH) + 1 < len(self.minH):
            val = -1 * heapq.heappop(self.minH)
            heapq.heappush(self.maxH, val)

        if len(self.minH) + 1 < len(self.maxH):
            val = heapq.heappop(self.maxH)
            heapq.heappush(self.minH, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.maxH) > len(self.minH):
            return (self.maxH[0])
        if len(self.minH) > len(self.maxH):
            return (-1 * self.minH[0])
        
        return ((self.maxH[0] + (-1 * self.minH[0])) / 2)
        


        
        