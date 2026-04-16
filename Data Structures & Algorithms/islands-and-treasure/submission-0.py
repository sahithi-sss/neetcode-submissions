class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #single source BFS soln
        if not grid :
            return None
        rows, cols = len(grid), len(grid[0])
        def bfs(row,col):
            q = deque([(row,col,0)])
            visited = set()
            visited.add((row,col))
            while q:
                r,c,val = q.popleft()
                lst = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in lst:
                    nr, nc = r+dr, c+dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] != -1 and (nr,nc) not in visited:
                        grid[nr][nc] = min(grid[nr][nc], val + 1)
                        visited.add((nr,nc))
                        q.append((nr,nc,val+1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row,col)
