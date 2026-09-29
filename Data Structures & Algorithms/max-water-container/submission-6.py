class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights)-1, 0

        while l < r:
            area = min(heights[r], heights[l]) * (r-l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            res = max(area, res)
        
        return res

