class Solution:
    def dfs(self, r,c,grid,visited):
        rows = len(grid)
        cols = len(grid[0])
        
        if r<0 or r == rows or c < 0 or c == cols:
            return
        if grid[r][c] == 0 or visited[r][c] == 1:
            return

        visited[r][c] = 1
        self.dfs(r+1,c,grid,visited)
        self.dfs(r,c+1,grid,visited)
        self.dfs(r,c-1,grid,visited)
        self.dfs(r-1,c,grid,visited)

        
    def numEnclaves(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for c in range(cols):
            if grid[0][c] == 1 and visited[0][c] == 0:
                self.dfs(0,c,grid,visited)
            if grid[rows-1][c] == 1 and visited[rows-1][c] == 0:
                self.dfs(rows-1,c,grid,visited)
        
        for r in range(rows):
            if grid[r][0] == 1 and visited[r][0] == 0:
                self.dfs(r,0,grid,visited)
            if grid[r][cols-1] == 1 and visited[r][cols-1] == 0:
                self.dfs(r,cols-1,grid,visited)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count +=1

        return count
        