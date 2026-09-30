class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            
            for w2, u2 in edges[n1]:
                if w2 not in visit:
                    heapq.heappush(minHeap, (w1 + u2, w2))
        
        return t if len(visit) == n else -1



