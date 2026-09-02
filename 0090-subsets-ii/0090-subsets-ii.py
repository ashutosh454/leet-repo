class Solution:
    def generate(self,index,n,arr,sub,result):
        n=len(arr)
        if index >= n:
            result.append(sub.copy())
            return

        sub.append(arr[index])
        self.generate(index+1,n,arr,sub,result)
        sub.pop()
        while index+1 < n and arr[index] == arr[index+1]:
            index+=1
        self.generate(index+1,n,arr,sub,result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub=[]
        nums.sort()
        n=len(nums)
        ans=[]
        self.generate(0,n,nums,sub,ans)
        return ans
        