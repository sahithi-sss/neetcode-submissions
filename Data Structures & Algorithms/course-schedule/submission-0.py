class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        edges = []
        for src, dest in prerequisites:
            edges.append((dest, src, -1))  
            # <-- use weight -1 so cycles become negative cycles 
        dist = [0] * n
        for i in range(n - 1):
            repeat = False
            for u, v , wt in edges:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    repeat = True
            if not repeat:
                break
        # one more pass: if any relaxation possible => negative cycle => original graph had a cycle
        for u, v , wt in edges:
            if dist[u] + wt < dist[v]:
                return False
        return True
