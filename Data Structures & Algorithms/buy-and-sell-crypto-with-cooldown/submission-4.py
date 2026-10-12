class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}

        def backtrack(buy, i):
            if i >= len(prices):
                return 0

            if (buy, i) in dp:
                return dp[(buy, i)]
            
            cooldown=backtrack(buy,i+1)

            if buy:
                buying=(backtrack(not buy, i+1)-prices[i])
                dp[(buy, i)]=max(buying, cooldown)
            else:
                selling=(backtrack(not buy, i+2)+prices[i])
                dp[(buy, i)]=max(selling, cooldown)
            
            return dp[(buy, i)]
        
        return backtrack(True, 0)