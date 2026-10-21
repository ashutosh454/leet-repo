class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_dep = 0

        for ch in s:
            if ch == "(":
                count+=1
                max_dep = max(max_dep , count)
            elif ch == ")":
                count -=1
        
        return max_dep