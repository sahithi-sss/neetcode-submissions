class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def add_cell(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] != 1:
                return
            grid[r][c] = 2
            visited.add((r,c))
            q.append((r,c))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2 and (row,col) not in visited:
                    grid[row][col] = 2
                    visited.add((row,col))
                    q.append((row,col))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()        
                add_cell(r+1,c)
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r,c-1)
            dist += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return max(0,dist-1)