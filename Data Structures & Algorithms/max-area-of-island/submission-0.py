class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows , cols = len(grid), len(grid[0])

        visited = set()
        max_ar = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            ar = 1
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    new_r , new_c = row + dr, col + dc
                    if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r,new_c) not in visited):
                        visited.add((new_r,new_c))
                        ar += 1
                        q.append((new_r,new_c))
            return ar
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and (r,c) not in visited):
                    ar = bfs(r,c)
                    max_ar = max(ar,max_ar)

        return max_ar
