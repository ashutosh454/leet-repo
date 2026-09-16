class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for _ in range(cols)] for _ in range (rows)]
        distance = [[0 for _ in range(cols)] for _ in range (rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r,c,0])
                    visited[r][c] = 1
        
        while queue:
            x,y,dis = queue.popleft()
            distance[x][y] = dis
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x,new_y = x+dx , y+dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if visited[new_x][new_y] == 1:
                        continue
                    queue.append([new_x,new_y,dis+1])
                    visited[new_x][new_y] = 1
        return distance
