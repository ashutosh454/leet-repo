class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        def gain(A,B):
            max_gain = 0
            curr_gain = 0

            for a, b in zip(A,B):
                diff = b-a
                curr_gain = max(diff , curr_gain+diff)
                max_gain = max(max_gain, curr_gain)
            
            return sum(A) + max_gain
        
        return max(gain(nums1,nums2), gain(nums2,nums1))