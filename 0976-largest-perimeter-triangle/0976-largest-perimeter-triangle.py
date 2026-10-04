class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        max_peri = 0

        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]> nums[i+2] and nums[i] + nums[i+2] > nums[i+1] and nums[i+1]+nums[i+2]>nums[i]:
                total= nums[i]+nums[i+1]+nums[i+2]
                max_peri = max(max_peri,total)
        
        return max_peri
