class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prefix = 0
        max_prefix = 0
        min_prefix = 0

        for num in nums:
            prefix += num
            max_prefix = max(max_prefix , prefix)
            min_prefix = min(min_prefix, prefix)
        
        return max_prefix - min_prefix