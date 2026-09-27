from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_freq = 0

        for right in range(len(nums)):
            freq[nums[right]]+=1
            max_freq = max(max_freq,freq[nums[right]])

            while (right-left + 1) - max_freq > k:
                freq[nums[left]]-=1
                left +=1
        
        return max_freq
