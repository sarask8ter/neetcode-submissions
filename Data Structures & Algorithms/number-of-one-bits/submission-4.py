class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            bit = 1 & n
            res += bit
            n >>= 1
        
        return res