class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        max_length=0
        zero_count=0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            if zero_count > k:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
            
            window_size = right-left + 1
            max_length = max(max_length, window_size)
        return max_length


                