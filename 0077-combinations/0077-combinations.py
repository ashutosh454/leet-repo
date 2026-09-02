class Solution:
    def generate(self,index,n,k,sub,result):
        if len(sub) == k:
            result.append(sub.copy())
            return
        if index > n:
            return
        sub.append(index)
        self.generate(index+1,n,k,sub,result)
        sub.pop()
        self.generate(index+1,n,k,sub,result)

    def combine(self, n: int, k: int) -> List[List[int]]:
        sub=[]
        ans=[]
        self.generate(1,n,k,sub,ans)
        return ans

        