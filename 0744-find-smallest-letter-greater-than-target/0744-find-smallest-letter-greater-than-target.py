class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        upper_bound = 0
        low = 0
        high = len(letters)-1

        while low<=high:
            mid = (low+high)//2

            if letters[mid]>target:
                upper_bound=mid
                high = mid-1
            else:
                low=mid+1
        return letters[upper_bound]

        