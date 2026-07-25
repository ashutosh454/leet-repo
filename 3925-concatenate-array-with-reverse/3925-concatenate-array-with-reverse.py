class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        # left=0
        # right = len(nums)-1

        # while left<=right:
        #     nums[left],nums[right] = nums[right], nums[left]
        #     left+=1
        #     right-=1
        
        return nums+nums[::-1]
        