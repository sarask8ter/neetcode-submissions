class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = defaultdict(int)

        for i in range(len(s)):
            c = s[i]

            if c not in cnt:
                cnt[c] = i
            else:
                cnt[c] = len(s)
        
        res = len(s)
        for val in cnt.values():
            res = min(val, res)
        
        return -1 if res == len(s) else res
