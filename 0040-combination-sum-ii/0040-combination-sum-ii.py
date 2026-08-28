class Solution:
    def generate(self,index, nums, total, target, sub, result):
        
        
        if total == target:
            result.append(sub.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return

        sum = total + nums[index]
        sub.append(nums[index])
        self.generate(index+1, nums, sum, target, sub, result)
        sub.pop()
        sum = total
        next_index = index+1
        while next_index < len(nums) and nums[next_index] == nums[index]:
            next_index+=1    

        self.generate(next_index, nums, sum, target, sub, result)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub=[]
        result=[]
        candidates.sort()

        self.generate(0, candidates, 0, target, sub, result)
        
        return result