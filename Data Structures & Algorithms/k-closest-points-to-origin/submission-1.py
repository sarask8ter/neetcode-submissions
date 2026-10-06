class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            d = (math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(minHeap, (d, [x, y]))
        
        res = []
        while k:
            d, point = heapq.heappop(minHeap)
            res.append(point)
            k -= 1

        return res
            

