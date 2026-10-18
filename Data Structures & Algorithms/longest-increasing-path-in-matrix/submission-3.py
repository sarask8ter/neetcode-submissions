class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        # [7,7,5]
        # [2,4,6]
        # [8,2,0]

        def dfs(r, c, prev):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1 + max(dfs(r+1, c, matrix[r][c]), dfs(r, c+1, matrix[r][c]), dfs(r-1, c, matrix[r][c]), dfs(r, c-1, matrix[r][c]))

            dp[(r, c)] = res
            return dp[(r, c)]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c, float("-inf")), res)
        
        return res
            
            


