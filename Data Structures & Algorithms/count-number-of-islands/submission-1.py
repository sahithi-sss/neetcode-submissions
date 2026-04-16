class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        def bfs(row,col):
            q = collections.deque()
            q.append((row,col))
            visit.add((row,col))
            while q:
                r,c = q.popleft()
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr, dc in directions:
                    r1 , c1 = r+dr , c+dc
                    if (r1 in range(rows)) and (c1 in range(cols)) and (grid[r1][c1] == "1") and ((r1,c1) not in visit ):
                        visit.add((r1,c1))
                        q.append((r1,c1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    bfs(row,col)
                    islands += 1
        return islands