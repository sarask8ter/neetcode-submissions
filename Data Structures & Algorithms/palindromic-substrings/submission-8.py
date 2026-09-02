class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalis(st, l, r):
            cnt = 0

            while l >= 0 and r < len(st) and st[l] == st[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        
        for i in range(len(s)):
            res += countPalis(s, i, i)
            res += countPalis(s, i, i+1)
        
        return res
            
