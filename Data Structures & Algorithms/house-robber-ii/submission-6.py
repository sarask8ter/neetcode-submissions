class Solution:
    def rob(self, nums: List[int]) -> int:
        # either you take from the end or not but it includes the first one
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        

        def helper(num):
            if not num:
                return None

            if len(num) == 1:
                return num[0]

            dp = len(num) * [0]
            dp[0] = num[0]
            dp[1] = max(num[0], num[1])

            for i in range(2, len(num)):
                dp[i] = max(dp[i-1], dp[i-2]+num[i])
            
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[0:len(nums)-1]))