class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            mid = l + ((r-l) // 2)
            totalH = 0
            for b in piles:
                totalH += math.ceil(b/mid)
            if (totalH <= h):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res


