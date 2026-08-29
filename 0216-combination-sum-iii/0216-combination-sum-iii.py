class Solution:
    def generate(self, index, total, target, arr, sub, result, k):
        if total == target:
            if len(sub) == k:
                result.append(sub.copy())
                return
        if index >= len(arr) or total>target or len(sub)>k:
            return
        
        sub.append(arr[index])
        sum = total + arr[index]

        self.generate(index+1, sum, target, arr, sub, result, k)
        sub.pop()
        sum=total
        self.generate(index+1, sum, target, arr, sub, result, k)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sub=[]
        result=[]
        nums=[1,2,3,4,5,6,7,8,9]

        self.generate(0, 0, n, nums, sub, result, k)
        return result