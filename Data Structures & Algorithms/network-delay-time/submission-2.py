class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visit = set()
        minHeap = [(0, k)]

        for u, v, w in times:
            adj[u].append((v, w))
        
        t = 0

        while minHeap:
            d1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            t = d1

            for n2, d2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (d2 + d1, n2))
        
        return t if len(visit) == n else -1
