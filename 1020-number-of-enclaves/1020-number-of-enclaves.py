class Solution:
    def dfs(self, r,c,grid,visited,rows,cols):
        rows = len(grid)
        cols = len(grid[0])
        
        if r<0 or r == rows or c < 0 or c == cols:
            return
        if grid[r][c] == 0 or visited[r][c] == 1:
            return
        visited[r][c] = 1
        self.dfs(r+1,c,grid,visited,rows,cols)
        self.dfs(r,c+1,grid,visited,rows,cols)
        self.dfs(r,c-1,grid,visited,rows,cols)
        self.dfs(r-1,c,grid,visited,rows,cols)
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        if not grid or not grid[0]:
            return 0

        r,c=0,0
        for c in range(cols):
            if grid[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r,c,grid,visited,rows,cols)
        r,c=rows-1,0
        for c in range(cols):
            if grid[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r,c,grid,visited,rows,cols)
        r,c=0,0
        for r in range(rows):
            if grid[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r,c,grid,visited,rows,cols)
        r,c=0,cols-1
        for r in range(rows):
            if grid[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r,c,grid,visited,rows,cols)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count +=1

        return count
        