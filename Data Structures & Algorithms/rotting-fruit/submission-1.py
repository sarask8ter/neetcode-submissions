class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # need to do bfs with neighbors
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        nei = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh > 0:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in nei:
                    if r+dr >= 0 and c+dc >= 0 and r+dr < ROWS and c+dc < COLS and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
                        q.append([r+dr, c+dc])
                
            res += 1
        
        return res if fresh == 0 else -1
        
        
