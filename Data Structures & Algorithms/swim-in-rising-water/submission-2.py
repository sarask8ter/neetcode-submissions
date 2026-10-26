class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visit = set()

        visit.add((0, 0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                dir_R, dir_C = r + dr, c + dc

                if dir_R < 0 or dir_C < 0 or dir_R == N or dir_C == N or (dir_R, dir_C) in visit:
                    continue

                visit.add((dir_R, dir_C))
                heapq.heappush(minHeap, [max(t, grid[dir_R][dir_C]), dir_R, dir_C])




