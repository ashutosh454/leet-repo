from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegree[u]+=1

        queue = deque()
        result = []

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            current_subject = queue.popleft()
            result.append(current_subject)
            for adjNode in adj_list[current_subject]:
                indegree[adjNode] -=1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)
        
        if len(result) == numCourses:
            return result
        else:
            return []