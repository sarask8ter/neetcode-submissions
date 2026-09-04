class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP, minP = 1, 1
        res = float("-inf")

        for num in nums:
            tmp = num * maxP # -3
            maxP = max(num * maxP, num, num * minP)
            minP = min(tmp, num, num * minP)
            res = max(res, maxP)
        
        return res

