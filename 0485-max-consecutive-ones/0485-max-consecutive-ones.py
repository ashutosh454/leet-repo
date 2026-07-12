class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one=0
        count=0

        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                count = 0
            max_one = max(max_one, count)
        return max_one