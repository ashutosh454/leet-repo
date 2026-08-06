class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m=len(potions)
        result=[]

        for spell in spells:
            low =0
            high = m-1
            lb = m

            while low<=high:
                mid = (low+high)//2

                if potions[mid]*spell>=success:
                    lb=mid
                    high = mid-1
                else:
                    low = mid+1

            result.append(m-lb)
        return result