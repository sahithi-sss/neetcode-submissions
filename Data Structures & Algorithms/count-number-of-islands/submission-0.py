class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows , cols = len(grid) , len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    m_r , m_c = row + dr, col + dc
                    if (m_r in range(rows) and m_c in range(cols) and grid[m_r][m_c] == "1" and (m_r,m_c) not in visited):
                        q.append((m_r, m_c))
                        visited.add((m_r, m_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands

        