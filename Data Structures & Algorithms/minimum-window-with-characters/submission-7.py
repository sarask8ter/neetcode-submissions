class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        want, window = {}, {}

        for c in t:
            want[c] = 1 + want.get(c, 0)
        
        need, have = len(want), 0

        res = [-1, -1]
        minLen=float("inf")

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in want and window[s[r]] == want[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < minLen:
                    minLen=(r-l+1)
                    res=[l, r]
                
                window[s[l]] -= 1
                
                if s[l] in want and window[s[l]] + 1 == want[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l:r+1] if minLen < float("inf") else ""


        

