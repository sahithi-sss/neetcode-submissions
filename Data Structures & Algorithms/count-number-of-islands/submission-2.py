class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])
        tot = 0
        visited = []
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            visited.append((row,col))
            while q:
                r,c = q.popleft()
                lst = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in lst:
                    nr , nc = r+dr, c+dc
                    if nr>= 0 and nc>= 0 and nr < rows and nc < cols and (nr,nc) not in visited and grid[nr][nc] == "1":
                        visited.append((nr,nc))
                        q.append((nr,nc))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and ((row,col) not in visited):
                    bfs(row,col)
                    tot += 1
        return tot