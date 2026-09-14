class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        image_copy = deepcopy(image)
        initial_color = image_copy[sr][sc]
        queue = deque()
        queue.append((sr,sc))
        if initial_color == color:
            return image
        
        image_copy[sr][sc] = color

        while queue:
            i,j = queue.popleft()
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i,new_j = i+dx , j+dy
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if image_copy[new_i][new_j] == initial_color:
                        image_copy[new_i][new_j] = color
                        queue.append((new_i,new_j))

        return image_copy


        
                
