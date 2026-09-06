class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = defaultdict(int)

        for c in s:
            cnt[c] = 1 + cnt.get(c, 0)
        
        idx = 0

        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        
        return -1






