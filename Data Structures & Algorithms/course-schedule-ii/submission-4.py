class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * (numCourses)

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, res = 0, []
        while q:
            crs = q.popleft()
            res.append(crs)
            finish += 1

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        if finish != numCourses:
            return []

        return res
            

