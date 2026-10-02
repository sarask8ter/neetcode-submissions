class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res, stack = [], ["JFK"]
        edges = defaultdict(list)

        for from_i, to_i in sorted(tickets)[::-1]:
            edges[from_i].append(to_i)

        while stack:
            cur = stack[-1]

            if edges[cur]:
                stack.append(edges[cur].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]
