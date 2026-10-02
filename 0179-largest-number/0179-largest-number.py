class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        n = len(nums)

        for i in range(n):
            for j in range(n-i-1):
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    str_nums[j],str_nums[j+1] = str_nums[j+1],str_nums[j]
                
        if str_nums[0] == "0":
            return "0"
        
        return "".join(str_nums)