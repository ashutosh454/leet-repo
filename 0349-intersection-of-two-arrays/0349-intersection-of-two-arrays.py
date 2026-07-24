class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        nums3= set(nums1)
        nums4= set(nums2)

        for num in nums3:
            if num in nums4:
                result.add(num)
        return list(result)
        