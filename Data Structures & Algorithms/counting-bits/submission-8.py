class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n+1):
            cnt = 0
            while num:
                bit = 1 & num
                cnt += bit
                num >>= 1
            res.append(cnt)
        
        return res
