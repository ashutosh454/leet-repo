class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        r,c = 0,0
        m,n = len(grid),len(grid[0])
        visited = {(0,0)}

        directions = {
            'L' : (0,-1),
            'R' : (0,1),
            'U' : (-1,0),
            'D' : (1,0)
        }

        while True:
            char = grid[r][c]
            dr , dc = directions[char]
            nr, nc = r + dr, c+dc

            if not(0<= nr <m and 0<= nc < n) or (nr,nc) in visited:
                break
            visited.add((nr,nc))
            r,c = nr,nc
        return [r,c]
