from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[u].append(v)
            indegree[v]+=1
        
        queue = deque()
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            current_node = queue.popleft()
            count +=1

            for adjNode in adj_list[current_node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)
        
        return count == numCourses

