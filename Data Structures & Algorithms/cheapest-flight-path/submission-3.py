class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        edges = [[] for _ in range(n)]

        for u, v, cst in flights:
            edges[u].append([v, cst])
        
        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k: continue
        
            for nei, w in edges[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))
        return prices[dst] if prices[dst] != float("inf") else -1            
