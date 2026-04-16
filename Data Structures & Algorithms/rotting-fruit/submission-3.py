class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        tm = 0 # tot time
        row,col = len(grid), len(grid[0])

        cnt = 0 # count of fresh fruits
        #(i,j) for all rotten fruits - queue
        rotten = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    cnt += 1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        #visited = [] not needed over here
        #also, always use set for visited, not list  -> else O(1) lookups
        while rotten and cnt >0:
        #while rotten : would inc time even in the case when cnt == 0 but queue is not empty
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                #visited.append((r,c))
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<= nr < row and 0<= nc < col and grid[nr][nc] == 1:
                        cnt -= 1
                        grid[nr][nc] = 2
                        rotten.append((nr,nc))
            tm += 1

        return -1 if cnt != 0 else tm