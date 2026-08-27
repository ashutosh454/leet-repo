class Solution:
    def solution(self, index, candidates, target, sub, result):
        if target == 0:
            result.append(sub.copy())
            return

        if target < 0 or index>=len(candidates):
            return

        sub.append(candidates[index])
        self.solution(index, candidates, target-candidates[index], sub, result)
        sub.pop()

        self.solution(index+1, candidates, target, sub, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        sub=[]
        self.solution(0, candidates, target, sub, ans)
        return ans