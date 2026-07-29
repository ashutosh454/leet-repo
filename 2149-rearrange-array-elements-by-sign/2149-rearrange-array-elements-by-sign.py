from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [0]*n

        even_index = 0
        odd_index = 1

        for num in nums:
            if num>0:
                ans[even_index] = num
                even_index+=2
            if num<0:
                ans[odd_index] = num
                odd_index+=2
        return ans