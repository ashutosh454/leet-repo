class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[[]]

        for num in nums:
            new_subset=[]

            for curr in subsets:
                new_subset.append(curr + [num])
            
            subsets.extend(new_subset)

        return subsets