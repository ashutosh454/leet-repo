class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        
        nums.sort()
        total_sum = sum(nums)

        for i in range(len(nums)-1,-1,-1):
            sum_smaller = total_sum - nums[i]

            if sum_smaller > nums[i]:
                return total_sum
            
            total_sum -= nums[i]
        
        return -1
