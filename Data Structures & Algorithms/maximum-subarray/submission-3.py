class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cnt = 0

        for num in nums:
            if cnt < 0:
                cnt = 0

            cnt += num
            maxSub = max(cnt, maxSub)
        
        return maxSub