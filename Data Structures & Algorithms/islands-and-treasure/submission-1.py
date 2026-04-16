class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multi src BFS
        rows,cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def add_cell(r,c):
            if (min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        #all the places where there exists a treasure chest is stored
        # in the visited set and queue
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add_cell(r+1,c)
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r,c-1)
            dist += 1
        # after iterating through all the squares that can be traversed by moving
        # one step from this "treasure chest" square, their respective
        #distances are increased by 1