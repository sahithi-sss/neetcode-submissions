class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        area = []
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            ar = 1
            while q:
                rw,cl = q.popleft()
                drcns = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in drcns:
                    r1 , c1 = rw + dr, cl+dc
                    if (r1 in range(rows)) and (c1 in range(cols)) and (grid[r1][c1] == 1) and ((r1,c1) not in visit) :
                        ar += 1
                        visit.add((r1,c1))
                        q.append((r1,c1))
            area.append(ar)
        for r in range(rows) :
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    bfs(r,c)
        return max(area) if area else 0