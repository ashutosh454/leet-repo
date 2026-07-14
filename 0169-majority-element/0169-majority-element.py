class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        majority_threshold = len(nums) // 2
        
        for num in nums:
            
            counts[num] = counts.get(num, 0) + 1
            
            
            if counts[num] > majority_threshold:
                return num