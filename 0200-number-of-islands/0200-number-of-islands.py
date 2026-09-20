class Solution:
    def search(self,r,c,visited,grid):
        rows = len(grid)
        cols = len(grid[0])
        
        if r<0 or r == rows or c<0 or c == cols:
            return 
        if visited[r][c] == 1 or grid[r][c] == '0':
            return
        visited[r][c] = 1
        self.search(r+1,c,visited,grid)
        self.search(r,c+1,visited,grid)
        self.search(r,c-1,visited,grid)
        self.search(r-1,c,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        if not grid:
            return 0
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == '1':
                    self.search(r,c,visited,grid)
                    count+=1
        
        return count




        