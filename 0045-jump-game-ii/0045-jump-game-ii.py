class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)

        if n<=1:
            return 0
        jumps=0
        current_range_end=0
        farthest_reach=0

        for i in range(n-1):
            farthest_reach=max(farthest_reach, i+nums[i])

            if i == current_range_end:
                jumps+=1
                current_range_end = farthest_reach

                if current_range_end >= n-1:
                    return jumps
        