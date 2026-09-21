from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        # 0 for uncolored, 1 for color A and -1 for color B
        for i in range(n):
            if color[i] !=0:
                continue
            color[i] = 1
            queue = deque([i])

            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == 0:
                        color[neighbour] = 0 - color[node]
                        queue.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False
            
        return True