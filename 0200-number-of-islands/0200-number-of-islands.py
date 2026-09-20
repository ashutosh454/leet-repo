class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def helper(r,c):
            if r < 0 or r == rows or c < 0 or c == cols:
                return
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            helper(r+1,c)
            helper(r,c+1)
            helper(r,c-1)
            helper(r-1,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count +=1
                    helper(r,c)
                    
        return count