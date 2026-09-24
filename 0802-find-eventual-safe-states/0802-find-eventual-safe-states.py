from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        v = len(graph)
        adj_list = [[] for _ in range(v)]

        for node in range(v):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)

        queue = deque()

        indegree = [0 for _ in range(v)]
        for node in range(v):
            for adjNode in adj_list[node]:
                indegree[adjNode] +=1

        for node in range(v):
            if indegree[node] == 0:
                queue.append(node)

        result = []
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegree[adjNode] -=1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)
        
        result.sort()
        return result


