class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for row in range(1, m):
            cur = [1] * n
            for col in range(1, n):
                cur[col] = (prev[col] + cur[col-1])
            prev = cur
        
        return prev[n-1]
