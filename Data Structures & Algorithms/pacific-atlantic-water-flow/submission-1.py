class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prevht):
            if (r,c) in visit or r < 0 or c< 0 or r>= rows or c >= cols or heights[r][c] < prevht:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for col in range(cols):
            dfs(0,col,pac,heights[0][col])
            dfs(rows-1,col,atl,heights[rows-1][col])
        for row in range(rows):
            dfs(row,0,pac,heights[row][0])
            dfs(row,cols -1,atl,heights[row][cols-1])
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    res.append((row,col))
        return res