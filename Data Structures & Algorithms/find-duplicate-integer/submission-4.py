class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n-1

        while low < high:
            mid = low + ((high - low) // 2)
            lessThanOrEqual = sum(1 for num in nums if num <= mid)
            
            if lessThanOrEqual > mid:
                high = mid
            else:
                low = mid + 1
        
        return low

        # low, high = 1, 4
        # lessthanorequal = 4
        # mid = 2



