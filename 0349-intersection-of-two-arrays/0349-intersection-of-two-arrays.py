class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        nums3= set(nums1)
        nums4= set(nums2)

        for num1 in nums2:
            for num2 in nums3:
                if num1==num2:
                    result.add(num1)
        return list(result)
        